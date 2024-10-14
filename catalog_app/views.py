from rest_framework import generics
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from catalog_app.models import SaleItem, Sale
from catalog_app.serializers import SaleItemSerializer, CategorySerializer, SalesSerializer
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


@extend_schema(tags=["catalog"], responses=SalesSerializer)
class SaleApi(APIView):
    def get(self, request: Request) -> Response:
        sale = Sale.objects.first()
        serialized = SalesSerializer(sale, many=False)
        return Response(serialized.data)

