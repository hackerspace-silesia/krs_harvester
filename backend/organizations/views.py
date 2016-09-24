from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ReadOnlyModelViewSet
from organizations.models import Organization
from organizations.serializers import (
    OrganizationSerializer,
    OrganizationDetailSerializer,
)


class OrganizationViewSet(ReadOnlyModelViewSet):
    queryset = Organization.objects
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self, *args, **kwargs):
        if 'pk' in self.kwargs:
            return OrganizationDetailSerializer
        return OrganizationSerializer
