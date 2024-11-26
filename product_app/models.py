from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    fullDescription = models.TextField(null=True, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    freeDelivery = models.BooleanField(default=True)
    count = models.SmallIntegerField(default=1)
    # Automatically set the field to now when the object is first created.
    date = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.DecimalField(default=5, max_digits=2, decimal_places=1)
    # Добавляем новое поле для хранения количества отзывов
    reviews_count = models.IntegerField(default=0)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True
    )
    tags = models.ManyToManyField("Tag", related_name="products")

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=32)
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="subcategories",
    )

    def __str__(self):
        return self.title


def product_image_directory_path(instance: "ProductImage", filename):
    return f"products/images/{filename}"


def category_image_directory_path(instance: "CategoryImage", filename: str) -> str:
    return f"categories/images/{filename}"


def get_default_alt() -> str:
    return "image"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="product",
        null=True,
    )
    src = models.ImageField(upload_to=product_image_directory_path)
    alt = models.CharField(max_length=32, default=get_default_alt, null=True)

    def __str__(self):
        return str(self.product)


class CategoryImage(models.Model):
    category = models.OneToOneField(
        Category, on_delete=models.CASCADE, related_name="image", null=True
    )
    src = models.ImageField(upload_to=category_image_directory_path)
    alt = models.CharField(max_length=32, default=get_default_alt, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=12)
    # product = models.ManyToManyField(
    #     Product, related_name="tags", verbose_name="product"
    # )

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.CharField(max_length=48)
    email = models.EmailField(blank=True, null=True)
    text = models.TextField()
    rate = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)],
        default=1,
    )
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(
        to=Product, related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.author}, {self.product}"


class Specification(models.Model):
    name = models.CharField(max_length=32)
    value = models.CharField(max_length=32)
    product = models.ForeignKey(
        to=Product,
        related_name="specifications",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.product}, {self.name},  {self.value}"
