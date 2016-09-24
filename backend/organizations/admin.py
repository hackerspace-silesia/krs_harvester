from django.contrib import admin
from organizations.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_zero_krs', 'city', 'zip_code', 'address')
