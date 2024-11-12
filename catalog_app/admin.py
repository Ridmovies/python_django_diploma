from django.contrib import admin

from catalog_app.models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass
