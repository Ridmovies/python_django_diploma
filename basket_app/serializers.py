from rest_framework import serializers

from basket_app.models import Order


class OrderProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="product")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "createdAt",
            "fullName",
            "email",
            "deliveryType",
            "paymentType",
            "totalCost",
            "status",
            "city",
            "address",
            "products",
        )
