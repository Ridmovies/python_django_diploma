from django.db import models

from product_app.models import Product


class SaleItem(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=True)
    salePrice = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    dateFrom = models.DateTimeField()
    dateTo = models.DateTimeField()
    sale = models.ForeignKey(to="Sale", related_name="items", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.product}, "


class Sale(models.Model):
    title = models.CharField(max_length=128, default="Sale!!!")

    def __str__(self):
        return f"{self.title}"
