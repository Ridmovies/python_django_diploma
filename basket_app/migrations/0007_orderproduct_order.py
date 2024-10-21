# Generated by Django 5.1.2 on 2024-10-21 08:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket_app', '0006_alter_order_address_alter_order_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='basket_app.order'),
        ),
    ]