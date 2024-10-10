from django.contrib import admin

from product_app.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    pass



