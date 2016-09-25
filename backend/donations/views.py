from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from donations.models import Donator
from donations.serializers import DonatorSerializer


class DonatorViewSet(ReadOnlyModelViewSet):
    queryset = Donator.objects.all()
    serializer_class = DonatorSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name',)
