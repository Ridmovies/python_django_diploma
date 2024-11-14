from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from product_app.models import Product, Review, Tag
from product_app.serializers import (
    ProductFullSerializer,
    ReviewSerializer,
    TagSerializer,
)
# from product_app.tasks import update_product_avg_rating
from product_app.services import update_product_avg_rating


@extend_schema(tags=["product"], responses=ProductFullSerializer)
class ProductDetailApiView(RetrieveAPIView):
    # queryset = Product.objects.all()
    queryset = Product.objects.prefetch_related(
        'images',
        'tags',
        'reviews',
        'specifications',
    ).all()
    serializer_class = ProductFullSerializer
    lookup_field = "id"


@extend_schema(tags=["product"], responses=ReviewSerializer)
class AddProductReviewApiView(APIView):
    def post(self, request: Request, id: int):
        review = Review.objects.create(**request.data, product_id=id)
        # TODO Celery task
        # update_product_avg_rating.delay(id)
        update_product_avg_rating(id)
        serializer = ReviewSerializer(review, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(tags=["tags"])
class TagsListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
