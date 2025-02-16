from typing import Any, Dict
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.contrib.admin.sites import AdminSite

from .models import App
from .admin import AppAdmin, verify_apps

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


class AdminVerificationTest(TestCase):
    """
    Test suite for the admin verification process.
    """

    def setUp(self) -> None:
        """
        Set up a superuser and two sample app instances for admin verification.
        """
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='adminpass',
            email='admin@example.com'
        )
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.app1: App = App.objects.create(
            title='App 1',
            description='Description 1',
            price='1.99',
            owner=self.user,
            is_verified=False
        )
        self.app2: App = App.objects.create(
            title='App 2',
            description='Description 2',
            price='2.99',
            owner=self.user,
            is_verified=False
        )

    def test_verify_apps_admin_action(self) -> None:
        """
        Test that the custom admin action marks the selected apps as verified.
        """
        site: AdminSite = AdminSite()
        app_admin: AppAdmin = AppAdmin(App, site)
        queryset = App.objects.filter(id__in=[self.app1.id, self.app2.id])
        # Simulate calling the admin action; request is not used so we pass None.
        verify_apps(app_admin, None, queryset)
        # Refresh the instances from the database.
        self.app1.refresh_from_db()
        self.app2.refresh_from_db()
        self.assertTrue(self.app1.is_verified)
        self.assertTrue(self.app2.is_verified)


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
