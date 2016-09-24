from django.contrib import admin
from donations.models import Donation, Donator


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'donator', 'organization', 'money', 'date')


@admin.register(Donator)
class DonatorAdmin(admin.ModelAdmin):
    list_display = ('name',)
