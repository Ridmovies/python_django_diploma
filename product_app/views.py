from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from product_app.models import Product, Review, Tag
from product_app.serializers import ProductFullSerializer, ReviewSerializer, TagSerializer


@extend_schema(tags=["product"], responses=ProductFullSerializer)
class ProductDetailApiView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer
    lookup_field = 'id'


# @extend_schema(tags=["product"], responses=ReviewSerializer)
# class AddProductReviewApiView(CreateAPIView):
#     serializer_class = ReviewSerializer
#


@extend_schema(tags=["product"], responses=ReviewSerializer)
class AddProductReviewApiView(APIView):
    def post(self, request: Request, id:int):
        review = Review.objects.create(**request.data, product_id=id)
        serializer = ReviewSerializer(review, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(tags=["tags"])
class TagsListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
