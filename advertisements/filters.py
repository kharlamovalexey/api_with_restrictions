from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = filters.DateTimeFromToRangeFilter(field_name="created_at")
    updated_at = filters.DateTimeFromToRangeFilter(field_name="updated_at")

    class Meta:
        model = Advertisement
        fields = ["created_at", "updated_at", "status", "creator"]
