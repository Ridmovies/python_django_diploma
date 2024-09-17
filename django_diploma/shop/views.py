from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import Group, User

from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Product, Category
from shop.serializers import (
    UserSerializer,
    GroupSerializer,
    ProductSerializer,
    CategorySerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryListView(ListView):
    model = Category


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



# python manage.py create_products