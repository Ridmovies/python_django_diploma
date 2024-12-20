# Generated by Django 5.1.2 on 2024-10-16 09:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("fullName", models.CharField(max_length=128, null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("phone", models.CharField(max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Avatar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("src", models.ImageField(upload_to="avatar_image_directory_path")),
                ("alt", models.CharField(default="avatar", max_length=12)),
                (
                    "profile",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auth_app.profile",
                    ),
                ),
            ],
        ),
    ]
