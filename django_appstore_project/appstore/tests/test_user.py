from typing import Any, Dict
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class UserAuthTests(APITestCase):
    """
    Test suite for the user registration (signup) and login endpoints.
    """

    def test_signup_creates_user(self) -> None:
        """
        Test that a new user is created via the signup endpoint.
        """
        url: str = reverse('signup')
        data: Dict[str, Any] = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login_returns_token(self) -> None:
        """
        Test that valid login credentials return an authentication token.
        """
        # Create a test user first
        User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )
        url: str = reverse('login')
        data: Dict[str, Any] = {
            "username": "testuser",
            "password": "testpassword"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the response contains a token
        self.assertIn('token', response.data)
