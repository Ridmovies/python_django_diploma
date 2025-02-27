# Generated by Django 5.1.2 on 2024-10-13 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_app", "0017_alter_categoryimage_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categoryimage",
            name="category",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="image",
                to="product_app.category",
            ),
        ),
    ]
