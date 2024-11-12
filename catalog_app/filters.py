from django.db.models import QuerySet
from rest_framework import generics, filters
from rest_framework.filters import OrderingFilter


class CustomOrdering(OrderingFilter):
    def get_ordering(self, request, queryset, view) -> list:

        sorting_by = request.query_params.get("sort", None)
        sorting_type = request.query_params.get("sortType", None)
        ordering = super().get_ordering(request, queryset, view)

        if sorting_by:
            if sorting_type:
                if sorting_type == "inc":
                    ordering = [f"-{sorting_by}"]
                if sorting_type == "dec":
                    ordering = [f"{sorting_by}"]
        return ordering


class IsOwnerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(price__gte=11)


class TagFilterBackend(filters.BaseFilterBackend):
    """
    Filter tag
    """

    def filter_queryset(self, request, queryset, view) -> QuerySet:
        tags = request.query_params.getlist("tags[]", None)
        if tags:
            tags = [int(tag) for tag in tags]
            return queryset.filter(tags__id__in=tags)
        return queryset


class FreeDeliveryFilterBackend(filters.BaseFilterBackend):
    """
    Filter free_delivery
    """

    def filter_queryset(self, request, queryset, view) -> QuerySet:
        free_delivery = request.query_params.get("filter[freeDelivery]", None)
        if free_delivery is not None:
            if free_delivery == "true":
                return queryset.filter(freeDelivery=True)
            if free_delivery == "false":
                return queryset.filter(freeDelivery=False)
        return queryset


class AvailableFilterBackend(filters.BaseFilterBackend):
    """
    Filter free_delivery
    """

    def filter_queryset(self, request, queryset, view) -> QuerySet:
        is_available = request.query_params.get("filter[available]", None)
        if is_available is not None:
            if is_available == "true":
                return queryset.filter(count__gt=0)
            if is_available == "false":
                return queryset.filter(count=0)
        return queryset


class MinPriceFilterBackend(filters.BaseFilterBackend):
    """
    Filter free_delivery
    """

    def filter_queryset(self, request, queryset, view) -> QuerySet:
        min_price = request.query_params.get("filter[minPrice]", None)
        if min_price is not None:
            return queryset.filter(price__gte=min_price)
        return queryset


class MaxPriceFilterBackend(filters.BaseFilterBackend):
    """
    Filter free_delivery
    """

    def filter_queryset(self, request, queryset, view) -> QuerySet:
        max_price = request.query_params.get("filter[maxPrice]", None)
        if max_price is not None:
            return queryset.filter(price__lte=max_price)
        return queryset


class CategoryFilterBackend(filters.BaseFilterBackend):
    """
    Filter free_delivery
    """

    def filter_queryset(self, request, queryset, view) -> QuerySet:
        try:
            category = request.META.get("HTTP_REFERER", None).split("/")[4]
            if category is not None:
                return queryset.filter(category=category)
        except Exception as e:
            return queryset
