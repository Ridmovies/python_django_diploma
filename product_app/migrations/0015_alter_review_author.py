# Generated by Django 5.1.2 on 2024-10-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0014_specification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.CharField(max_length=48),
        ),
    ]