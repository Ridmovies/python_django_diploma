from django.contrib import admin

from product_app.models import (
    Product,
    Category,
    ProductImage,
    Tag,
    Review,
    Specification,
    CategoryImage,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


@admin.register(CategoryImage)
class CategoryImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    pass

