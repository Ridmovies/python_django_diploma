# Generated by Django 5.1.2 on 2024-10-14 07:34

from django.db import migrations, models

import product_app.models


class Migration(migrations.Migration):

    dependencies = [
        ("product_app", "0018_alter_categoryimage_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productimage",
            name="alt",
            field=models.CharField(
                default=product_app.models.get_default_alt, max_length=32, null=True
            ),
        ),
    ]
