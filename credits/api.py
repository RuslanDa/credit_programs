from .models import Organization, Offer
from rest_framework import viewsets, permissions
from .serializers import OrganizationSerializer, OfferSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    permissions_classes = [
        permissions.AllowAny,
    ]
    serializer_class = OrganizationSerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    permissions_classes = [
        permissions.AllowAny,
    ]
    serializer_class = OfferSerializer
