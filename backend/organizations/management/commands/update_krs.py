from django.core.management.base import BaseCommand
from organizations.models import Organization
import requests

URL = 'https://api-v3.mojepanstwo.pl/dane/krs_podmioty.json'

class Command(BaseCommand):

    def get_chunk_data(self, url=None):
        """
         :return: tuple of list of objects and next url
         :rtype: (list, (str|None))
        """
        if url is None:
            req = requests.get(URL, params={
                'conditions[krs_podmioty.forma_prawna_typ_id]': '2',
                'limit': 1000,
            })
        else:
            req = requests.get(url)
        req.raise_for_status()
        data = req.json()
        return data['Dataobject'], data['Links'].get('next')

    def get_data(self):
        url = None
        while True:
            data, url = self.get_chunk_data(url)
            for single_data in data:
                yield single_data['data']
            self.stdout.write('.', ending='')
            self.stdout.flush()
            if url is None:
                break

    def handle(self, *args, **kwargs):
        for data in self.get_data():
            d = lambda x: data['krs_podmioty.%s' % x]
            kwargs = dict(
                name=d('nazwa'),
                krs=int(d('krs')),
                street=u'{} {}'.format(d('adres_ulica'), d('adres_numer')),
                zip_code=d('adres_kod_pocztowy'),
                city=d('adres_miejscowosc'),
                aim=d('cel_dzialania'),
                wojewodztwo=d('wojewodztwo_id'),
                powiat=d('powiat_id'),
                gmina=d('gmina_id'),
            )
            org_query = Organization.objects.filter(krs=kwargs['krs'])

            if org_query.count() == 0:
                Organization.objects.create(**kwargs)
            else:
                org_query.update(**kwargs)

        self.stdout.write('\nDone')
