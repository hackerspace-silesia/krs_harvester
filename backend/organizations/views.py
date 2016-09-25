from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import (
    SearchFilter,
    DjangoFilterBackend,
    OrderingFilter
)
from organizations.models import Organization
from organizations.serializers import (
    OrganizationSerializer,
    OrganizationDetailSerializer,
)


class OrganizationViewSet(ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    search_fields = ('name', 'krs', 'city')
    filter_fields = ('krs', 'city', 'wojewodztwo', 'powiat', 'gmina')

    def get_serializer_class(self, *args, **kwargs):
        if 'pk' in self.kwargs:
            return OrganizationDetailSerializer
        return OrganizationSerializer
