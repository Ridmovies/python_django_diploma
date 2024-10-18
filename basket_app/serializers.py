from rest_framework import serializers

from basket_app.models import Order, Basket


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            # "createdAt",
            # "fullName",
            # "email",
            # "deliveryType",
            # "paymentType",
            # "totalCost",
            # "status",
            # "city",
            # "address",
            # "products",
        )


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ("id",)

