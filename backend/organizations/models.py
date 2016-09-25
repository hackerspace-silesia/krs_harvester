from __future__ import unicode_literals

from django.db import models
from uuid import uuid4


class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=150)
    krs = models.IntegerField(unique=True)
    street = models.CharField(max_length=300, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=200, blank=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True, blank=True)
    aim = models.TextField(blank=True)
    wojewodztwo = models.IntegerField(null=True, blank=True)
    powiat = models.IntegerField(null=True, blank=True)
    gmina = models.IntegerField(null=True, blank=True)
    #todo: ?

    def get_zero_krs(self):
        return str(self.krs).zfill(10)

    def __unicode__(self):
        return self.name


class Keywords(models.Model):
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization)
