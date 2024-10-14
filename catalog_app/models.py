from django.db import models

from product_app.models import Product


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    salePrice = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    dateFrom = models.DateTimeField()
    dateTo = models.DateTimeField()

    def __str__(self):
        return f"{self.product}"

