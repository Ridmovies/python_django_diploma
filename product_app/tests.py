import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from product_app.models import Product, Tag, Review


def create_product():
    return Product.objects.create(
        title='Test product',
        price=1111,
        count=5,
        rating=5,
    )


def create_tag():
    return Tag.objects.create(
        name='Test tag',
    )


class ProductTests(APITestCase):
    def setUp(self):
        self.product = create_product()

    def test_get_product_detail(self):
        url = reverse("product:product_detail", kwargs={"id": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 1)


class TagsTests(APITestCase):
    def setUp(self):
        self.tag = create_tag()

    def test_get_tags_list(self):
        url = reverse('product:tags')
        response = self.client.get(url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tag.objects.count(), 1)
        self.assertDictEqual({'id': 1, 'name': 'Test tag'}, data[0])


class ReviewTests(APITestCase):
    def setUp(self):
        self.product = create_product()

    def test_post_product_review(self):
        url = reverse("product:add_review", kwargs={"id": 1})
        review_data = {
          "author": "string",
          "email": "user@example.com",
          "text": "string",
          "rate": 5,
          "product_id": 1
        }
        response = self.client.post(url, review_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 1)

