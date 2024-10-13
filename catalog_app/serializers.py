from rest_framework import serializers

from catalog_app.models import SaleItem
from product_app.models import Category, CategoryImage


class SaleItemSerializer(serializers.ModelSerializer):
    # images = ImageSerializer(many=True)

    class Meta:
        model = SaleItem
        fields = (
            # "price",
            "salePrice",
            "dateFrom",
            "dateTo",
            # "title",
            # "images",
        )


class CatImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImage
        fields = ("src", "alt")


class SubCategorySerializer(serializers.ModelSerializer):
    image = CatImageSerializer(many=False, required=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "image",
        )


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)
    image = CatImageSerializer(many=False, required=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "image",
            "subcategories",
        )

