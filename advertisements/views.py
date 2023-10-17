from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
# from rest_framework.

from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend,] 
    filterset_class = AdvertisementFilter
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwner()]
        return []


