from .models import Organization, Offer, Partner, Checklist
from rest_framework import viewsets, permissions
from .serializers import OrganizationSerializer, OfferSerializer, PartnerSerializer, ChecklistSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows organizations to be viewed or edited.
    '''
    queryset = Organization.objects.all()
    permissions_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = OrganizationSerializer


class OfferViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows offers to be viewed or edited.
    '''
    queryset = Offer.objects.all()
    permissions_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = OfferSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows partners to be viewed or edited.
    '''
    queryset = Partner.objects.all()
    permissions_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = PartnerSerializer


class ChecklistViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows checklists to be viewed or edited.
    '''
    queryset = Checklist.objects.all()
    permissions_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ChecklistSerializer
