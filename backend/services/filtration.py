from django_filters import rest_framework as filters

from apps.cards.models import Card


class CardFilter(filters.FilterSet):

    number = filters.CharFilter(field_name='number', lookup_expr='contains')
    series = filters.CharFilter(field_name='series', lookup_expr='contains')

    min_issue_date = filters.DateTimeFilter(field_name='issue_date', lookup_expr='qte')
    max_issue_date = filters.DateTimeFilter(field_name='issue_date', lookup_expr='lte')

    min_expiration_date = filters.DateTimeFilter(field_name='expiration_date', lookup_expr='qte')
    max_expiration_date = filters.DateTimeFilter(field_name='expiration_date', lookup_expr='lte')


    class Meta:
        fields = ('number', 'series', 'status',)
        model = Card