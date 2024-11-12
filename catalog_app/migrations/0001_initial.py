# Generated by Django 5.1.2 on 2024-10-14 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("product_app", "0019_alter_productimage_alt"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "salePrice",
                    models.DecimalField(decimal_places=2, default=0, max_digits=8),
                ),
                ("dateFrom", models.DateTimeField()),
                ("dateTo", models.DateTimeField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product_app.product",
                    ),
                ),
            ],
        ),
    ]
