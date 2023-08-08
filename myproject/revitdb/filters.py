import django_filters
from .models import Room

class RoomFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Room
        fields = ['project_info', 'level']


