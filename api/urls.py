from django.urls import include, path
from rest_framework import routers

from .views import WhViewSet, VehicleViewSet, ServicesViewSet, ClientsReviewsViewSet, PartnerViewSet, TopBrandsViewSet

router = routers.DefaultRouter()
router.register(r'hero', WhViewSet)
router.register(r'vehicle', VehicleViewSet)
router.register(r'service', ServicesViewSet)
router.register(r'client', ClientsReviewsViewSet)
router.register(r'partner', PartnerViewSet)
router.register(r'brand', TopBrandsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
