from django.db import models


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

    # def __str__(self):
    #     return f"{self.title}, "
