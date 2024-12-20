# Generated by Django 5.1.2 on 2024-10-18 11:54

from django.db import migrations, models

import auth_app.models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_app", "0004_remove_avatar_profile_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="avatar",
            name="src",
            field=models.ImageField(
                upload_to=auth_app.models.avatar_image_directory_path
            ),
        ),
    ]
