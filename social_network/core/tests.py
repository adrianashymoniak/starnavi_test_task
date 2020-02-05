from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.utils import json

from core.models import Post
from core.serializers import PostSerializer


class BaseTest(TestCase):
    def setUp(self):
        self.client.post(
            '/auth/register/',
            data=json.dumps(
                {
                    "username": "new_user",
                    "email": "new_user@test.com",
                    "password": "test",
                    "password2": "test"}
            ),
            content_type="application/json"
        )


class SignUpTest(TestCase):
    def test_register_a_user_with_valid_data(self):
        response = self.client.post(
            '/auth/register/',
            data=json.dumps(
                {
                    "username": "new_user",
                    "email": "new_user@test.com",
                    "password": "test",
                    "password2": "test"}
            ),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginTest(BaseTest):
    def test_login_user_with_valid_credentials(self):
        response = self.client.post(
            '/auth/login/',
            data=json.dumps(
                {
                    "username": "new_user",
                    "password": "test"}
            ),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreatePostTest(BaseTest):
    def test_create_post(self):
        self.client.post(
            '/auth/login/',
            data=json.dumps(
                {
                    "username": "new_user",
                    "password": "test"}
            ),
            content_type="application/json"
        )

        response = self.client.post(
            '/posts/',
            data=json.dumps(
                {"title": "test",
                 "description": "test",
                 "likes": []}
            ),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
