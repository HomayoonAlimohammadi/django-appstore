from typing import Any, Dict
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from ..models import App

User = get_user_model()

class AppCreationAPITest(APITestCase):
    """
    Test suite for the app creation API endpoint.
    """

    def setUp(self) -> None:
        """
        Set up a test user and log in.
        """
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.create_url: str = reverse('app-create')

    def test_create_app_success(self) -> None:
        """
        Test that an authenticated user can successfully create an app.
        """
        payload: Dict[str, Any] = {
            'title': 'Test App',
            'description': 'A sample test app',
            'price': '9.99'
        }
        response = self.client.post(self.create_url, data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(App.objects.count(), 1)
        app_instance = App.objects.first()
        assert app_instance is not None
        self.assertEqual(app_instance.owner, self.user)
        self.assertFalse(app_instance.is_verified)

    def test_create_app_without_authentication(self) -> None:
        """
        Test that an unauthenticated user cannot create an app.
        """
        self.client.logout()
        payload: Dict[str, Any] = {
            'title': 'Test App',
            'description': 'A sample test app',
            'price': '9.99'
        }
        response = self.client.post(self.create_url, data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
