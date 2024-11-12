import datetime

from rest_framework import serializers

from product_app.models import Product, ProductImage, Tag, Review, Specification


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("src", "alt")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


class ReviewSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Review
        fields = (
            "author",
            "email",
            "text",
            "rate",
            "date",
            "product_id",
        )

    def get_date(self, instance) -> str:
        return datetime.datetime.strftime(instance.date, "%d.%m.%Y %H:%M")


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = (
            "name",
            "value",
        )


class ProductFullSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, required=True)
    tags = TagSerializer(many=True, required=False)
    reviews = ReviewSerializer(many=True, required=False)
    specifications = SpecificationSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "price",
            "category",
            "date",
            "count",
            "description",
            "fullDescription",
            "freeDelivery",
            "images",
            "tags",
            "reviews",
            "specifications",
            "rating",
        )
