from django.contrib.auth.models import User
from django.db import models

from product_app.models import Product


class Basket(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} basket"


class Order(models.Model):
    # Оформление заказа
    createdAt = models.DateTimeField(auto_now_add=True)
    # example: 2023 - 05 - 05 12: 12
    fullName = models.CharField(max_length=128, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=11, null=True)
    deliveryType = models.CharField(max_length=12, null=True)
    paymentType = models.CharField(max_length=12, null=True)
    totalCost = models.FloatField(null=True)
    # example: 567.8
    status = models.CharField(max_length=12, null=True)
    city = models.CharField(max_length=24, null=True)
    address = models.CharField(max_length=64, null=True)
    # products =


class OrderProduct(models.Model):
    # product = models.ForeignKey(to=Product, on_delete=models.PROTECT)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    basket = models.ForeignKey(to=Basket, on_delete=models.CASCADE, related_name="products", null=True)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name="products", null=True)


class Payment(models.Model):
    # Todo add validators
    number = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    month = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    code = models.CharField(max_length=30)

