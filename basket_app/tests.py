import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from basket_app.models import Basket
from product_app.models import Product


def create_product():
    product = Product.objects.create(
        title="Test product",
        price=1111,
        count=5,
        rating=5,
    )
    return product


def create_product2():
    product2 = Product.objects.create(
        title="Test product2",
        price=2222,
        count=5,
        rating=5,
    )
    return product2


class BasketTests(APITestCase):
    def setUp(self):
        url = reverse("auth:registration")
        payload = b'{"name":"user7","username":"user7","password":"user7"}'
        response = self.client.post(url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.product = create_product()
        self.product2 = create_product2()
        self.url = reverse("basket_app:basket")

    def test_get_empty_basket(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Basket.objects.count(), 1)
        data = json.loads(response.content)
        self.assertEqual(data, [])

    def test_add_product_in_basket(self):
        data = {"id": self.product.id, "count": 2}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = json.loads(response.content)
        self.assertEqual(response_data[0]["id"], self.product.id)
        self.assertEqual(response_data[0]["count"], 2)

    def test_add_two_different_product_in_basket(self):
        data = {"id": self.product.id, "count": 2}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data2 = {"id": self.product2.id, "count": 2}
        response = self.client.post(self.url, data2, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = json.loads(response.content)
        self.assertEqual(len(response_data), 2)

    def test_add_two_same_product_in_basket(self):
        data = {"id": self.product.id, "count": 2}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = {"id": self.product.id, "count": 2}
        response = self.client.post(self.url, data, format="json")
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(response_data, {"message": "Product already in basket"})
        self.assertEqual(len(response_data), 1)

    def test_add_too_mach_product_in_basket(self):
        data = {"id": self.product.id, "count": 6}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        response_data = json.loads(response.content)
        self.assertEqual(response_data, {"message": "You can order only 5 products."})

    def test_delete_product_from_basket(self):
        data = {"id": self.product.id, "count": 2}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = json.loads(response.content)
        self.assertEqual(len(response_data), 1)
        response = self.client.delete(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(len(response_data), 0)


class OrderTests(APITestCase):
    def setUp(self):
        url = reverse("auth:registration")
        payload = b'{"name":"user7","username":"user7","password":"user7"}'
        response = self.client.post(url, data=payload, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.product = create_product()
        self.product2 = create_product2()
        url = reverse("basket_app:basket")
        data = {"id": self.product.id, "count": 2}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_orders(self):
        url = reverse("basket_app:orders")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(len(response_data), 0)

    def test_create_order(self):
        url = reverse("basket_app:orders")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(response_data, {"orderId": 1})

    def test_get_order_detail(self):
        url = reverse("basket_app:orders")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(response_data, {"orderId": 2})

        url = reverse("basket_app:order_detail", kwargs={"id": 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["id"], 2)

    def test_post_order_detail(self):
        url = reverse("basket_app:orders")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(response_data, {"orderId": 3})

        url = reverse("basket_app:order_detail", kwargs={"id": 3})
        data = {
            "fullName": "sting",
            "phone": "sting",
            "email": "exeample@example.com",
            "city": "sting",
            "address": "sting",
            "totalCost": 567.8,
            "paymentType": "online",
            "deliveryType": "free",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse("basket_app:order_detail", kwargs={"id": 3})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(response_data["id"], 3)
        self.assertEqual(response_data["totalCost"], 567.8)
