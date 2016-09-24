from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ReadOnlyModelViewSet
from donations.models import Donator
from donations.serializers import DonatorSerializer


class DonatorViewSet(ReadOnlyModelViewSet):
    queryset = Donator.objects
    serializer_class = DonatorSerializer
