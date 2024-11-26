from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.filters import SearchFilter

from catalog_app.filters import (
    AvailableFilterBackend,
    CategoryFilterBackend,
    CustomOrdering,
    FreeDeliveryFilterBackend,
    MaxPriceFilterBackend,
    MinPriceFilterBackend,
    TagFilterBackend,
)
from catalog_app.models import Sale
from catalog_app.pagination import CustomPagination
from catalog_app.serializers import CategorySerializer, SaleSerializer
from product_app.models import Category, Product
from product_app.serializers import ProductFullSerializer
from python_django_diploma.settings import BANNERS_AMOUNT, LIMITED_COUNT, POPULAR_RATING, CACHE_MIDDLEWARE_SECONDS


@extend_schema(tags=["catalog"], responses=ProductFullSerializer)
class PopularProductsListApi(generics.ListAPIView):
    queryset = Product.objects.filter(
        rating__gte=POPULAR_RATING,
        reviews_count__gte=1,
    )
    serializer_class = ProductFullSerializer


@extend_schema(tags=["catalog"], responses=ProductFullSerializer)
class LimitedProductsListApi(generics.ListAPIView):
    queryset = Product.objects.filter(count__lte=LIMITED_COUNT)
    serializer_class = ProductFullSerializer


@extend_schema(tags=["catalog"], responses=ProductFullSerializer)
class BannerListApi(generics.ListAPIView):
    # символ "?" означает, что результаты будут отсортированы в случайном порядке
    queryset = Product.objects.all().order_by("?")[:BANNERS_AMOUNT]
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
    search_fields = ["title"]
    filter_backends = [
        CustomOrdering,
        SearchFilter,
        TagFilterBackend,
        FreeDeliveryFilterBackend,
        AvailableFilterBackend,
        MinPriceFilterBackend,
        MaxPriceFilterBackend,
        CategoryFilterBackend,
    ]
