from django.core.management.base import BaseCommand
from organizations.models import Organization, Keyword

import re

re_split = re.compile(ur'[\s_,.;:]+')
re_is_number = re.compile(ur'\d+')


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Keyword.objects.all().delete()  # delete old keywords
        for org in Organization.objects.filter(aim__isnull=False):
            raw_keywords = set(
                raw_keyword.upper() for raw_keyword in
                re_split.split(org.aim)
                if not re_is_number.match(raw_keyword)
            )
            keywords = [
                Keyword(name=key, organization=org)
                for key in raw_keywords
            ]
            Keyword.objects.bulk_create(keywords)

        self.stdout.write('\nDone')
