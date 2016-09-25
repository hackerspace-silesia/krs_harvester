from django.db.models.aggregates import Sum, Avg, Max, Min, Count
from django.db.models.expressions import F
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.filters import (
    SearchFilter,
    DjangoFilterBackend,
    OrderingFilter
)

from donations.models import Donator, Donation
from donations.serializers import DonatorSerializer, DonationAggSerializer


class DonatorViewSet(ReadOnlyModelViewSet):
    queryset = Donator.objects.all()
    serializer_class = DonatorSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)


class DonationAggViewSet(ListModelMixin, GenericViewSet):
    queryset = (
        Donation.objects
        .select_related('organization', 'donator')
        .all()
    )
    serializer_class = DonationAggSerializer
    GROUP_FIELDS = {
        'wojewodztwo': 'organization__wojewodztwo',
        'powiat': 'organization__powiat',
        'gmina': 'organization__gmina',
        'city': 'organization__city',
        'donator': 'donator__name',
        'date': 'date',
    }
    NON_F_FIELDS = ['date']
    AGG_FIELDS = {
        'sum_money': Sum('money'),
        'avg_money': Avg('money'),
        'min_money': Min('money'),
        'max_money': Max('money'),
        'count_donations': Count('id'),
    }
    ALL_FIELDS = GROUP_FIELDS.copy()
    ALL_FIELDS.update({
        key: key for key in AGG_FIELDS.keys()
    })

    def get_group_fields(self):
        group = self.request.query_params.get('group', '')
        striped_fields = [field.strip() for field in group.split(',')]
        fields = {
            field: self.ALL_FIELDS.get(field)
            for field in striped_fields
        }
        return {
            key: value for key, value in fields.items() if value is not None
        }

    def get_ordering_fields(self):
        group = self.request.query_params.get('ordering', '')
        striped_fields = [field.strip() for field in group.split(',')]
        fields = [
            '-' + self.ALL_FIELDS.get(field[1:])
            if field[0:1] == '-'
            else self.ALL_FIELDS.get(field)
            for field in striped_fields
        ]
        return [field for field in fields if field]

    def get_filter_fields(self):
        params = self.request.query_params
        fields = {
            self.ALL_FIELDS.get(field.strip()): value
            for field, value in params.items()
        }
        return {
            key: value for key, value in fields.items() if key is not None
        }

    def get_queryset(self):
        fields = self.get_group_fields()
        annotate_fields = {
            name: F(key) for name, key in fields.items()
        }
        aliased_fields = {
            name: key for name, key in annotate_fields.items()
            if name not in self.NON_F_FIELDS
        }
        return (
            super(DonationAggViewSet, self)
            .get_queryset()
            .annotate(**aliased_fields)
            .values(*annotate_fields.keys())
            .annotate(**self.AGG_FIELDS)
            .order_by(*self.get_ordering_fields())
            .filter(**self.get_filter_fields())
        )

    def get_serializer(self, *args, **kwargs):
        kwargs = kwargs.copy()
        kwargs['fields'] = self.get_group_fields().keys() + self.AGG_FIELDS.keys()
        return super(DonationAggViewSet, self).get_serializer(*args, **kwargs)
