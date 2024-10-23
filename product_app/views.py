from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView

from product_app.models import Product, Review, Tag
from product_app.serializers import ProductFullSerializer, ReviewSerializer, TagSerializer


@extend_schema(tags=["product"], responses=ProductFullSerializer)
class ProductDetailApiView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer
    lookup_field = 'id'


@extend_schema(tags=["product"], responses=ReviewSerializer)
class AddProductReviewApiView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


@extend_schema(tags=["tags"])
class TagsListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
