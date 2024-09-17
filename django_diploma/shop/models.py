from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=True)
    fullDescription = models.TextField(null=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    freeDelivery = models.BooleanField(default=True)
    count = models.SmallIntegerField(default=1)
    # Automatically set the field to now when the object is first created.
    date = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.SmallIntegerField(
        null=True,
        validators=[MaxValueValidator(5), MinValueValidator(0)],
    )

    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)


class Category(models.Model):
    title = models.CharField(max_length=30)



# https://editor.swagger.io/?_gl=1*1uohfxh*_gcl_au*MTQyNTgyNTE3NC4xNzI2NDkwNjA4