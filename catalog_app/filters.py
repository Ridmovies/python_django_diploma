# from django_filters import NumberFilter
# from django_filters.rest_framework import BooleanFilter, FilterSet
from django.db.models import QuerySet
from rest_framework import generics, filters
from django_filters import rest_framework as django_filters

from product_app.models import Product


class CatalogFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    freeDelivery = django_filters.BooleanFilter(field_name='freeDelivery')
    available = django_filters.NumberFilter(field_name='count')

    class Meta:
        model = Product
        fields = (
            'min_price',
            'max_price',
            'freeDelivery',
            )

    @classmethod
    def filter_free_delivery(cls, queryset, name, value):
        # Здесь мы обрабатываем параметр filter[freeDelivery]
        if value is not None:
            if value == "true":
                return queryset.filter(freeDelivery=True)
            if value == "false":
                return queryset.filter(freeDelivery=False)
        return queryset

    @classmethod
    def filter_available(cls, queryset, name, value):
        if value:
            if value == "true":
                return queryset.filter(count__gt=0)
            if value == "false":
                return queryset.filter(count=0)
        return queryset

    @classmethod
    def filter_min_price(cls, queryset, name, value: int):
        if value:
            return queryset.filter(price__gte=value)
        return queryset

    @classmethod
    def filter_max_price(cls, queryset, value: int):
        if value:
            return queryset.filter(price__lte=value)
        return queryset

    @classmethod
    def filter_name(cls, queryset, value: str):
        if value:
            return queryset.filter(title=value)
        return queryset

    @classmethod
    def filter_sorting_by(cls, queryset: QuerySet, value: str, stype: str | None):
        if value:
            if stype == 'inc':
                return queryset.order_by(f'-{value}')
            if stype == 'dec':
                return queryset.order_by(value)
        return queryset




# /api/catalog/?filter[name]=&filter[minPrice]=0&filter[maxPrice]=50000&filter[fr
# eeDelivery]=false&filter[available]=true&currentPage=1&category=NaN&sort=price&sortType=inc&limit=20