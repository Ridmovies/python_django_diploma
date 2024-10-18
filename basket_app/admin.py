from django.contrib import admin

from basket_app.models import Order, Basket


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    pass



