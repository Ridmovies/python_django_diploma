# Generated by Django 5.1.2 on 2024-11-15 18:37

import product_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_app", "0024_remove_product_images_productimage_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categoryimage",
            name="alt",
            field=models.CharField(
                default=product_app.models.get_default_alt, max_length=32, null=True
            ),
        ),
    ]