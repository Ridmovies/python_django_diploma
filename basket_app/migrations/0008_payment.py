# Generated by Django 5.1.2 on 2024-10-21 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket_app', '0007_orderproduct_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('month', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=30)),
            ],
        ),
    ]
