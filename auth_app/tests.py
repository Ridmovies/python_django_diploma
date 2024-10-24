from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SignUpApiViewTests(APITestCase):
    def test_post_SignUpApiView(self):
        url = reverse("auth:registration")
        payload = b'{"name":"user7","username":"user7","password":"user7"}'
        response = self.client.post(url, data=payload, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = reverse("auth:profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_signup_view_with_invalid_data(self):
        url = reverse('auth:registration')
        payload = b'{"name":"user7","username":"","password":"user7"}'
        response = self.client.post(url, data=payload, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        url = reverse("auth:profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LogoutViewTest(APITestCase):
    def setUp(self):
        # Настройка начальных условий
        url = reverse("auth:registration")
        payload = b'{"name":"user7","username":"user7","password":"user7"}'
        response = self.client.post(url, data=payload, content_type='application/json')

    def test_logout(self):
        url = reverse("auth:profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('auth:logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse("auth:profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LoginApiViewTest(APITestCase):
    def setUp(self):
        url = reverse("auth:registration")
        payload = b'{"name":"user7","username":"user7","password":"user7"}'
        response = self.client.post(url, data=payload, content_type='application/json')

    def test_login(self):
        self.client.logout()

        url = reverse("auth:login")
        payload = b'{"name":"user7","username":"user7","password":"user7"}'
        response = self.client.post(url, data=payload, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse("auth:profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
