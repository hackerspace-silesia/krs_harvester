from rest_framework import serializers
from donations.models import Donation, Donator


class DonatorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donator
        fields = ('pk', 'name')


class DonatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donator


class DonationSerializer(serializers.ModelSerializer):
    donator = DonatorSimpleSerializer()

    class Meta:
        model = Donation
        fields = ('name', 'money', 'organization', 'donator')
