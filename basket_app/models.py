from django.contrib.auth.models import User
from django.db import models

from product_app.models import Product


class Basket(models.Model):
    user = models.OneToOneField(
        to=User, on_delete=models.CASCADE, null=True, blank=True
    )
    session_key = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f"{self.user} basket"


class Order(models.Model):
    # Оформление заказа
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    fullName = models.CharField(max_length=128, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=11, null=True)
    deliveryType = models.CharField(max_length=12, null=True)
    paymentType = models.CharField(max_length=12, null=True)
    totalCost = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    status = models.CharField(max_length=24, null=True)
    city = models.CharField(max_length=24, null=True)
    address = models.CharField(max_length=64, null=True)


class OrderProduct(models.Model):
    # product = models.ForeignKey(to=Product, on_delete=models.PROTECT)
    product_id = models.IntegerField()
    quantity = models.IntegerField(null=True)
    basket = models.ForeignKey(
        to=Basket, on_delete=models.CASCADE, related_name="products", null=True
    )
    order = models.ForeignKey(
        to=Order, on_delete=models.CASCADE, related_name="products", null=True
    )
