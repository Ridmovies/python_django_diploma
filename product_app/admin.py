from django.contrib import admin

from product_app.models import (
    Category,
    CategoryImage,
    Product,
    ProductImage,
    Review,
    Specification,
    Tag,
)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Количество пустых форм для добавления новых изображений
    min_num = 1  # Минимальное количество изображений
    max_num = 10  # Максимальное количество изображений


class CategoryImageInline(admin.TabularInline):
    model = CategoryImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    readonly_fields = ["rating", "reviews_count"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryImageInline]


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
