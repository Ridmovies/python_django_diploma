# Generated by Django 5.1.2 on 2024-10-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket_app', '0005_remove_orderproduct_product_orderproduct_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='deliveryType',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='fullName',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='paymentType',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='totalCost',
            field=models.FloatField(null=True),
        ),
    ]
