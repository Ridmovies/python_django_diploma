from rest_framework.serializers import ModelSerializer

from product_app.models import Product, ProductImage, Tag


class ImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("src", "alt")


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


class ProductFullSerializer(ModelSerializer):
    images = ImageSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'price',
            "category",
            "date",
            "count",
            "description",
            "fullDescription",
            "freeDelivery",
            "images",
            "tags",
            # "reviews",
            # "specifications",
            # "rating",
        )

