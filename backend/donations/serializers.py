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


class DonationAggSerializer(serializers.Serializer):
    sum_money = serializers.DecimalField(max_digits=12, decimal_places=2)
    avg_money = serializers.DecimalField(max_digits=12, decimal_places=2)
    min_money = serializers.DecimalField(max_digits=12, decimal_places=2)
    max_money = serializers.DecimalField(max_digits=12, decimal_places=2)
    count_donations = serializers.IntegerField()
    wojewodztwo = serializers.IntegerField()
    date = serializers.DateField()
    powiat = serializers.IntegerField()
    gmina = serializers.IntegerField()
    city = serializers.CharField()

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(DonationAggSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
