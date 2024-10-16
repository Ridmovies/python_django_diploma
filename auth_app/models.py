from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, primary_key=True)
    fullName = models.CharField(max_length=128, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=12, null=True)
    avatar = models.OneToOneField(to="Avatar", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user} profile"


class Avatar(models.Model):
    # profile = models.OneToOneField(to=Profile,
    #                                on_delete=models.CASCADE,
    #                                # related_name='avatar',
    #                                null=True)
    src = models.ImageField(upload_to="avatar_image_directory_path")
    alt = models.CharField(max_length=12, default="avatar")

    def __str__(self):
        return f"{self.alt}"


def avatar_image_directory_path(instance, filename):
    return f"avatars/images/{filename}"
