from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=True)
    fullDescription = models.TextField(null=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    freeDelivery = models.BooleanField(default=True)
    # TODO Create dynamic count
    count = models.SmallIntegerField(default=1)
    # Automatically set the field to now when the object is first created.
    date = models.DateTimeField(auto_now_add=True, null=True)
    # TODO Create dynamic rating
    rating = models.DecimalField(default=0.2, max_digits=2, decimal_places=1)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField("Tag", blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=32)
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="subcategories"
    )

    def __str__(self):
        return self.title


def product_image_directory_path(instance: "ProductImage", filename):
    return f"products/images/{filename}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name="product", null=True)
    src = models.ImageField(upload_to=product_image_directory_path)
    alt = models.CharField(max_length=32, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name

