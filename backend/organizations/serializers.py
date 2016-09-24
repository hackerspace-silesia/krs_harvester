from rest_framework import serializers
from organizations.models import Organization
from donations.serializers import DonationSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    krs = serializers.CharField(source='get_zero_krs')

    class Meta:
        model = Organization
        fields = (
            'pk', 'name', 'krs', 'address', 'zip_code',
            'city', 'lagitude', 'longtidue',
        )


class OrganizationDetailSerializer(OrganizationSerializer):
    donations = DonationSerializer(many=True)
