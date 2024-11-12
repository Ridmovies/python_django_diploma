from django.contrib import admin

from basket_app.models import Order, Basket, OrderProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    pass
