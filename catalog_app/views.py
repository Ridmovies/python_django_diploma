from django.db.models import QuerySet
from rest_framework import generics, status
from drf_spectacular.utils import extend_schema

from catalog_app.filters import CatalogFilter
from catalog_app.models import Sale
from catalog_app.pagination import CustomPagination
from catalog_app.serializers import CategorySerializer, SaleSerializer
from product_app.models import Product, Category
from product_app.serializers import ProductFullSerializer


@extend_schema(tags=["catalog"], responses=ProductFullSerializer)
class PopularProductsListApi(generics.ListAPIView):
    queryset = Product.objects.filter(rating__gte=4)
    serializer_class = ProductFullSerializer


@extend_schema(tags=["catalog"], responses=ProductFullSerializer)
class LimitedProductsListApi(generics.ListAPIView):
    queryset = Product.objects.filter(count__lte=5)
    serializer_class = ProductFullSerializer


@extend_schema(tags=["catalog"], responses=ProductFullSerializer)
class BannerListApi(generics.ListAPIView):
    queryset = Product.objects.all()[:1]
    serializer_class = ProductFullSerializer


@extend_schema(tags=["catalog"], responses=CategorySerializer)
class CategoriesListView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None).all()
    serializer_class = CategorySerializer


@extend_schema(tags=["catalog"], responses=SaleSerializer)
class SaleApi(generics.ListAPIView):
    queryset = Sale.objects.all().order_by("id")
    serializer_class = SaleSerializer
    pagination_class = CustomPagination


@extend_schema(tags=["catalog"], responses=ProductFullSerializer)
class CatalogView(generics.ListAPIView):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductFullSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        # Получаем параметры фильтрации из запроса
        free_delivery = self.request.query_params.get('filter[freeDelivery]', None)
        is_available = self.request.query_params.get('filter[available]', None)
        min_price = self.request.query_params.get('filter[minPrice]', None)
        max_price = self.request.query_params.get('filter[maxPrice]', None)
        name = self.request.query_params.get('filter[name]', None)
        sorting_by = self.request.query_params.get('sort', None)
        sorting_type = self.request.query_params.get('sortType', None)
        tags = self.request.query_params.getlist('tags[]', None)
        limit = self.request.query_params.get('limit', None)
        category = self.request.META['HTTP_REFERER'].split('/')[4]

        if 'filter=' in self.request.META['HTTP_REFERER']:
            filter_text = self.request.META['HTTP_REFERER'].split('=')[1]
            queryset: QuerySet = queryset.filter(title__contains=filter_text)

        if category:
            if str(category).isalnum():
                queryset = queryset.filter(category__id=int(category))

        if free_delivery is not None:
            queryset = CatalogFilter.filter_free_delivery(queryset, 'freeDelivery', free_delivery)

        if is_available is not None:
            queryset = CatalogFilter.filter_available(queryset, 'available', is_available)

        if min_price is not None:
            queryset = CatalogFilter.filter_min_price(queryset, 'min_price', int(min_price))

        if max_price is not None:
            queryset = CatalogFilter.filter_max_price(queryset, value=int(max_price))

        if name is not None:
            queryset = CatalogFilter.filter_name(queryset, value=name)

        if sorting_by:
            if sorting_type:
                queryset = CatalogFilter.filter_sorting_by(
                    queryset,
                    value=sorting_by,
                    stype=sorting_type,
                )

        if tags:
            tags = [int(tag) for tag in tags]
            queryset = queryset.filter(tags__id__in=tags)

        if limit:
            return queryset.distinct()[:int(limit)]
        # Для удаления дубликатов из QuerySet в Django можно использовать метод .distinct()
        return queryset.distinct()


