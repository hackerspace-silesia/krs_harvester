from rest_framework.viewsets import ReadOnlyModelViewSet
from organizations.models import Organization
from organizations.serializers import OrganizationSerializer


class OrganizationViewSet(ReadOnlyModelViewSet):
    queryset = Organization.objects
    serializer_class = OrganizationSerializer

    def get_serializer_class(self, *args, **kwargs):
        print args, kwargs
        return OrganizationSerializer

