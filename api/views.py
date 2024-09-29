from dealership.models import WellcomeHerro, Vehicles, Services, ClientsReviews, Partner, TopBrands
from rest_framework import permissions, viewsets
from rest_framework.decorators import permission_classes

from .serializers import HeroSerializer, VehiclesSerializer, ServicesSerializer, ClientsReviewsSerializer, PartnerSerializer, TopBrandsSerializer

class WhViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = WellcomeHerro.objects.all()
    serializer_class = HeroSerializer
    permission_classes = [permissions.IsAuthenticated]

class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer
    permission_classes = [permissions.IsAuthenticated]

class ServicesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientsReviewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ClientsReviews.objects.all()
    serializer_class = ClientsReviewsSerializer
    permission_classes = [permissions.IsAuthenticated]

class PartnerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [permissions.IsAuthenticated]

class TopBrandsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TopBrands.objects.all()
    serializer_class = TopBrandsSerializer
    permission_classes = [permissions.IsAuthenticated]
