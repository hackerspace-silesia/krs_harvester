from __future__ import unicode_literals

from django.db import models
from organizations.models import Organization


class Donator(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=150)


class Donation(models.Model):
    id = models.UUIDField(primary_key=True)
    donator = models.ForeignKey(Donator, related_name='donations')
    organization = models.ForeignKey(Organization, related_name='donations')
    name = models.CharField(max_length=150)
    money = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    with_day = models.BooleanField(default=True)
    with_month = models.BooleanField(default=True)

    #todo: ?
