from django.contrib import admin

from shop.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
