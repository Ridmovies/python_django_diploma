import json
import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.models import Avatar, Profile
from auth_app.serializers import ProfileSerializer
from django.conf import settings


class LoginApiView(APIView):
    @extend_schema(tags=["auth"])
    def post(self, request: Request) -> Response:
        # сначала мы декодируем данные из bytes-формата в строковой формат,
        # а затем используем их для десериализации в Python-объекты.
        decoded_data = json.loads(request.body.decode())
        username = decoded_data["username"]
        password = decoded_data["password"]

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response("Authentication successful", status=status.HTTP_200_OK)

        return Response("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)


class SignUpApiView(APIView):
    @extend_schema(tags=["auth"])
    def post(self, request: Request) -> Response:
        decoded_data = json.loads(request.body.decode())
        name = decoded_data["name"]
        username = decoded_data["username"]
        password = decoded_data["password"]

        try:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return Response(status=status.HTTP_201_CREATED)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutView(generics.GenericAPIView):
    serializer_class = None

    @extend_schema(tags=["auth"])
    def post(self, request: Request) -> Response:
        logout(request)
        return Response(status=status.HTTP_200_OK)


@extend_schema(tags=["profile"])
class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self) -> Profile:
        # Получаем профиль текущего пользователя
        profile: Profile = Profile.objects.get(user=self.request.user)
        return profile

    def post(self, request: Request) -> Response:
        data = request.data
        data.pop("avatar")
        # Получение профиля текущего пользователя
        profile: Profile = self.get_object()
        # Обновление полей профиля данными из запроса
        for key, value in data.items():
            setattr(profile, key, value)
        profile.save()
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)


class ProfileAvatarView(APIView):
    @extend_schema(tags=["profile"])
    def post(self, request: Request) -> Response:
        """Создание и обновление аватара"""
        # TODO Вынести в сервисный уровень проверку и удаление аватара
        file_obj = request.FILES["avatar"]

        # Установка максимального допустимого размера файла (например, 5 МБ)
        max_file_size = 5 * 1024 * 1024  # 5 MB

        # Проверяем размер файла
        if file_obj.size > max_file_size:
            raise ValidationError(f'Размер файла превышает {max_file_size / 1024 / 1024:.2f} МБ.')

        profile = Profile.objects.get(user=request.user)
        avatar: Avatar = Avatar.objects.create(src=file_obj)
        old_avatar_src = None
        if profile.avatar:
            old_avatar_src = settings.LOGIN_URL + str(profile.avatar.src)
        profile.avatar = avatar
        profile.save()
        if old_avatar_src:
            try:
                os.remove(old_avatar_src)
            except OSError as e:
                pass
        return Response(status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    @extend_schema(tags=["profile"])
    def post(self, request: Request) -> Response:
        user: User = User.objects.get(id=request.user.id)

        current_password = request.data.get("currentPassword", None)
        if current_password:
            is_valid = check_password(current_password, user.password)
            if not is_valid:
                return Response(
                    "Wrong current password", status=status.HTTP_409_CONFLICT
                )

        new_password = request.data.get("newPassword", None)
        if new_password:
            hashed_password = make_password(new_password)
            user.password = hashed_password
            user.save()
        return Response(status=status.HTTP_200_OK)
