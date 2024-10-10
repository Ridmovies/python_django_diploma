from rest_framework.serializers import ModelSerializer

from product_app.models import Product


class ProductFullSerializer(ModelSerializer):
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
            # "images",
            # "tags",
            # "reviews",
            # "specifications",
            # "rating",
        )
