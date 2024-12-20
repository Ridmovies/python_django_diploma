# Generated by Django 5.1.2 on 2024-10-16 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_app", "0002_alter_avatar_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="avatar",
            name="profile",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="auth_app.profile",
            ),
        ),
    ]
