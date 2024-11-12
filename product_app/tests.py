import json

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from product_app.models import Product, ProductImage, Review, Tag

test_img = (
    b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x05\x04\x04"
    b"\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44"
    b"\x01\x00\x03\x00\x54\x4e\x52\x45\x07\x88\xcc\x6f\x82\x84\x9b\xb1"
    b"\xaf\x25\xca\x07\x14\xec\x97\x33\x16\x13\x89\x93\x2d\x83\x79\x96"
    b"\xa7\x13\x05\x90\x17\x83\xc4\x99\xa6\x13\x05\x81\x19\x85\x95\x9d"
    b"\xae\x23\xeb\x9f\xaf\x27\xe9\xa3\xab\x29\xf3\xad\x2b\xfb\xae\x21"
    b"\xeb\x9b\xaf\x24\xe9\xa2\xac\x28\xf2\xaa\x22\xea\x98\xa7\x20\xe8"
    b"\xa0\xaa\x26\xf6\xa9\x24\xe4\x9c\xa4\x18\xe0\x9a\xa2\x1a\xe2\x9e"
    b"\xa6\x12\xe4\x92\xa0\x10\xe6\x94\xa8\x0e\xe6\x96\xa8\x0c\xe6\x98"
    b"\xaa\x08\xe6\x9a\xac\x06\xe6\x9c\xae\x04\xe6\x9e\xb0\x02\xe6\xa0"
    b"\xb2\x00\x3b"
)


def create_product():
    product = Product.objects.create(
        title="Test product",
        price=1111,
        count=5,
        rating=5,
    )
    # image_file = SimpleUploadedFile('test_img.jpg', test_img, content_type='image/gif')
    # ProductImage.objects.create(product=product, src=image_file, alt='Test Image')
    return product


def create_tag():
    return Tag.objects.create(
        name="Test tag",
    )


class ProductTests(APITestCase):
    def setUp(self):
        self.product = create_product()

    def test_get_product_detail(self):
        url = reverse("product:product_detail", kwargs={"id": self.product.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 1)


class TagsTests(APITestCase):
    def setUp(self):
        self.tag = create_tag()

    def test_get_tags_list(self):
        url = reverse("product:tags")
        response = self.client.get(url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tag.objects.count(), 1)
        self.assertDictEqual({"id": 1, "name": "Test tag"}, data[0])


class ReviewTests(APITestCase):
    def setUp(self):
        self.product = create_product()

    def test_post_product_review(self):
        url = reverse("product:add_review", kwargs={"id": self.product.id})
        review_data = {
            "author": "string",
            "email": "user@example.com",
            "rate": 4,
            "text": "string",
        }
        response = self.client.post(url, review_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 1)
