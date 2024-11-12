# Generated by Django 5.1.2 on 2024-10-11 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_app", "0007_remove_product_tags_tag_product"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tag",
            name="product",
        ),
        migrations.AddField(
            model_name="tag",
            name="product",
            field=models.ManyToManyField(
                related_name="tags", to="product_app.product", verbose_name="product"
            ),
        ),
    ]
