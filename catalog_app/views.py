from django.shortcuts import render
from rest_framework import generics
from drf_spectacular.utils import extend_schema

from catalog_app.models import SaleItem
from catalog_app.serializers import SaleItemSerializer
from product_app.models import Product
from product_app.serializers import ProductFullSerializer


@extend_schema(tags=["catalog"], responses=ProductFullSerializer)
class PopularProductsListApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer


@extend_schema(tags=["catalog"], responses=ProductFullSerializer)
class LimitedProductsListApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer


@extend_schema(tags=["catalog"], responses=ProductFullSerializer)
class BannerListApi(generics.ListAPIView):
    queryset = Product.objects.all()[:2]
    serializer_class = ProductFullSerializer


@extend_schema(tags=["catalog"], responses=SaleItemSerializer)
class SalesListApi(generics.ListAPIView):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer

