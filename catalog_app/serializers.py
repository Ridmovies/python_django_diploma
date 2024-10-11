from rest_framework import serializers

from catalog_app.models import SaleItem
from product_app.serializers import ImageSerializer


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
