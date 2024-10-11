from django.contrib import admin

from catalog_app.models import SaleItem


@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    pass
