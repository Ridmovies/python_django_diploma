from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from shop.models import Product, Category


class ProductListView(ListView):
    model = Product


class CategoryListView(ListView):
    model = Category


# python manage.py create_products