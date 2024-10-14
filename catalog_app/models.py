from django.db import models

from product_app.models import Product


class SaleItem(models.Model):
    # price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    # example: 500.67
    salePrice = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    # example: 200.67
    dateFrom = models.DateTimeField()
    dateTo = models.DateTimeField()
    # example: 05 - 20
    # title = models.CharField(max_length=32)
    # images[
    # xml: OrderedMap
    # {"wrapped": true}
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=True)
    sale = models.ForeignKey(to="Sale", related_name="items", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.product}, "


class Sale(models.Model):
    title = models.CharField(max_length=128, default="Sale!!!")
    # items = models.ManyToManyField(to=SaleItem, null=True)

    def __str__(self):
        return f"{self.title}"
