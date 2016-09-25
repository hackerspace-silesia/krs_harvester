from rest_framework import routers
from organizations.views import OrganizationViewSet
from donations.views import DonatorViewSet, DonationAggViewSet, DonationTotalAggViewSet


router = routers.SimpleRouter()
router.register('organizations', OrganizationViewSet)
router.register('donators', DonatorViewSet)
router.register('donations-agg', DonationAggViewSet)
router.register('donations-total', DonationTotalAggViewSet)
