# Generated by Django 5.1.2 on 2024-10-11 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleitem',
            name='price',
        ),
        migrations.RemoveField(
            model_name='saleitem',
            name='title',
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='salePrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
