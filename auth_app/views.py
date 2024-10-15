import json

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


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
            return Response('Authentication successful', status=status.HTTP_200_OK)

        return Response('Invalid credentials', status=status.HTTP_401_UNAUTHORIZED)


class SignUpApiView(APIView):
    @extend_schema(tags=["auth"])
    def post(self, request: Request) -> Response:
        decoded_data = json.loads(request.body.decode())
        name = decoded_data["name"]
        username = decoded_data["username"]
        password = decoded_data["password"]

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return Response(status=status.HTTP_200_OK)


class LogoutView(APIView):
    @extend_schema(tags=["auth"])
    def post(self, request: Request) -> Response:
        logout(request)
        return Response(status=status.HTTP_200_OK)

