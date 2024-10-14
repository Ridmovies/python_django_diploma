import datetime

from rest_framework import serializers

from catalog_app.models import SaleItem, Sale
from product_app.models import Category, CategoryImage
from product_app.serializers import ImageSerializer


class SaleItemSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="product.id", read_only=True)
    images = ImageSerializer(source="product.images", many=True, required=True)
    title = serializers.CharField(source="product.title", read_only=True)
    price = serializers.CharField(source="product.price", read_only=True)
    dateFrom = serializers.SerializerMethodField()
    dateTo = serializers.SerializerMethodField()

    class Meta:
        model = SaleItem
        fields = (
            "id",
            "price",
            "salePrice",
            "dateFrom",
            "dateTo",
            "title",
            "images",
        )

    def get_dateFrom(self, instance):
        return datetime.datetime.strftime(instance.dateFrom, '%d-%m')

    def get_dateTo(self, instance):
        return datetime.datetime.strftime(instance.dateTo, '%d-%m')


class SalesSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)
    # currentPage = serializers.IntegerField()
    # lastPage = serializers.IntegerField()

    class Meta:
        model = Sale
        fields = (
            "items",
            # "currentPage",
            # "lastPage",
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

