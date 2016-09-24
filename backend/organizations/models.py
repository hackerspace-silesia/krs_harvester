from __future__ import unicode_literals

from django.db import models


class Organization(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=150)
    krs = models.IntegerField()
    address = models.CharField(max_length=300, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=200, blank=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, null=True)
    #todo: ?

    def get_zero_krs(self):
        return str(self.krs).zfill(10)
