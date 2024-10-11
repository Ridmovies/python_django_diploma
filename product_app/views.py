from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from drf_spectacular.utils import extend_schema
from rest_framework import status, mixins
from rest_framework.generics import RetrieveAPIView, CreateAPIView, GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from product_app.models import Product, Review
from product_app.serializers import ProductFullSerializer, ReviewSerializer


@extend_schema(tags=["product"], responses=ProductFullSerializer)
class ProductDetailApiView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer
    lookup_field = 'id'


@extend_schema(tags=["product"], responses=ReviewSerializer)
class AddProductReviewApiView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
