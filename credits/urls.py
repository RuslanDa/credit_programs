from rest_framework import routers
from .api import OrganizationViewSet, OfferViewSet

router = routers.DefaultRouter()
router.register('api/orgs', OrganizationViewSet, 'orgs')
router.register('api/offers', OfferViewSet, 'offers')



urlpatterns = router.urls