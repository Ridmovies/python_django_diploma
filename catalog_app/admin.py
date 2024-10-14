from django.contrib import admin

from catalog_app.models import SaleItem, Sale


@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass
