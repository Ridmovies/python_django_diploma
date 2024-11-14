import datetime
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from catalog_app.models import Sale
from product_app.models import Category, Product
from python_django_diploma.settings import BANNERS_AMOUNT


class CatalogTests(APITestCase):
    def setUp(self):
        self.products = Product.objects.bulk_create(
            [
                Product(title="Test product 1", price=1111, count=7, rating=5),
                Product(title="Test product 2", price=1111, count=5, rating=5),
                Product(title="Test product 3", price=1111, count=3, rating=2),
            ]
        )

        self.sale = Sale.objects.create(
            product=self.products[0],
            salePrice=100,
            dateFrom=datetime.datetime.now(),
            dateTo=datetime.datetime.now(),
        )

        self.categories = Category.objects.bulk_create(
            [
                Category(title="Cats", parent=None),
                Category(title="Dogs", parent=None),
            ]
        )

    def test_get_banners(self):
        url = reverse("catalog:banners")
        response = self.client.get(url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), BANNERS_AMOUNT)

    def test_get_popular_products_list(self):
        url = reverse("catalog:popular")
        response = self.client.get(url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 2)

    def test_get_LimitedProductsListApi(self):
        url = reverse("catalog:limited")
        response = self.client.get(url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 2)

    def test_get_SaleApi(self):
        url = reverse("catalog:sales")
        response = self.client.get(url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data["items"]), 1)
        self.assertEqual(data["items"][0]["salePrice"], "100.00")

    def test_get_CategoriesListView(self):
        url = reverse("catalog:categories")
        response = self.client.get(url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["title"], "Cats")
