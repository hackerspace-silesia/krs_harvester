#-*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand
from datetime import date
from organizations.models import Organization
from donations.models import Donation, Donator
import requests

ROOT_URL = 'https://danepubliczne.gov.pl'
URL = ROOT_URL + '/api/3/action/package_show'
URL_ID = (
    'wykaz_organizacji_pozytku_publicznego__'
    'ktore_otrzymaly_1__naleznego_podatku_dochodowego_od_osob_fizy'
)
URL_REPORT = ROOT_URL + '/api/action/datastore_search'

class Command(BaseCommand):

    def get_report_data(self, url=None):
        """
         :rtype: list(str)
        """
        req = requests.get(URL, params={
            'id': URL_ID,
        })
        req.raise_for_status()
        data = req.json()
        return [
            (d['id'], int(d['name'][-7:-3]))
            for d in data['result']['resources']
            if d['name'].lower().startswith('wykaz opp')
        ]

    def get_chunk_data(self, report_id, url=None, session=None):
        """
         :return: tuple of list of objects and next url
         :rtype: (list, (str|None))
        """
        session = session or requests.Session()
        if url is None:
            req = session.get(URL_REPORT, params={
                'limit': 1000,
                'resource_id': report_id,
            })
        else:
            req = session.get(ROOT_URL + url)
        req.raise_for_status()
        data = req.json()['result']
        return data['records'], data['_links'].get('next')

    def get_data(self, report_id):
        url = None
        session = requests.Session()
        while True:
            data, url = self.get_chunk_data(report_id, url, session)
            if data is None:
                break
            for single_data in data:
                yield single_data
            self.stdout.write('.', ending='')
            self.stdout.flush()

    def get_data_from_reports(self):
        report_data = self.get_report_data()
        for report_id, year in report_data:
            for data in self.get_data(report_id):
                yield data, year

    def handle(self, *args, **kwargs):
        donator, _ = Donator.objects.get_or_create(name='1%')
        for data, year in self.get_data_from_reports():
            organization_kwargs = dict(
                name=data[u'Nazwa organizacji pożytku publicznego'],
                krs=data['Numer \nKRS']  # boze kto daje nowa linijke w nazwie pola?
            )

            org = Organization.objects.filter(
                krs=organization_kwargs['krs']
            ).first()
            if org is None:
                org = Organization.objects.create(**organization_kwargs)

            kwargs = dict(
                name='1%% PIT',
                money=data[u'Kwota w zł'],
                donator=donator,
                organization=org,
                date=date(year, 1, 1),
                with_day=False,
                with_month=False,
            )
            don_query = Donation.objects.filter(
                name=kwargs['name'],
                date=kwargs['date'],
                donator=donator,
                organization=org,
            )

            if don_query.count() == 0:
                Donation.objects.create(**kwargs)
            else:
                don_query.update(**kwargs)

        self.stdout.write('\nDone')
