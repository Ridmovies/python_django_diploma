# Generated by Django 5.1.2 on 2024-11-13 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("basket_app", "0012_alter_order_status"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Payment",
        ),
    ]