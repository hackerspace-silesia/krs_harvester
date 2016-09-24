from rest_framework import routers
from organizations.views import OrganizationViewSet
from donations.views import DonatorViewSet


router = routers.SimpleRouter()
router.register('organizations', OrganizationViewSet)
router.register('donators', DonatorViewSet)
