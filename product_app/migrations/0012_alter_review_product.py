# Generated by Django 5.1.2 on 2024-10-11 07:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_app", "0011_alter_review_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="product_app.product",
            ),
        ),
    ]
