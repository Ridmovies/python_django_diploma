import datetime

from rest_framework import serializers

from basket_app.models import Order, Basket, OrderProduct
from product_app.models import Product
from product_app.serializers import ImageSerializer, TagSerializer, ReviewSerializer


class ProductShortSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    tags = TagSerializer(many=True, required=False)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'price',
            "category",
            "date",
            "description",
            "freeDelivery",
            "images",
            "tags",
            "reviews",
            "rating",
        )

    def get_reviews(self, obj):
        return obj.reviews.count()


class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderProduct
        fields = (
            "product_id",
            "quantity",
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        product = Product.objects.get(id=representation['product_id'])  # Получаем продукт по id
        product_serializer = ProductShortSerializer(product)

        # Объединяем данные продукта и количество
        return {
            **product_serializer.data,
            "count": representation["quantity"]
        }


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(data="products", many=True)
    createdAt = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            "id",
            "createdAt",
            "fullName",
            "email",
            "phone",
            "deliveryType",
            "paymentType",
            "totalCost",
            "status",
            "city",
            "address",
            "products",
        )

    def get_createdAt(self, instance) -> str:
        # example: 2023 - 05 - 05 12: 12
        return datetime.datetime.strftime(instance.createdAt, '%Y-%m-%d %H:%M')


class BasketSerializer(serializers.ModelSerializer):
    products = ProductShortSerializer(data="products", many=True)

    class Meta:
        model = Basket
        fields = ("products",)

