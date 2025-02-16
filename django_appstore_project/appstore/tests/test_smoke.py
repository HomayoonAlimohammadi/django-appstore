from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.contrib.admin.sites import AdminSite

from ..models import App
from ..admin import AppAdmin, verify_apps

User = get_user_model()


class AppCreationAPITest(APITestCase):
    """
    Test suite for the app creation API endpoint.
    """

    def setUp(self) -> None:
        """
        Set up a test user and log in.
        """
        self.super_user = User.objects.create_user(username='admin', password='adminpass')
        self.test_user = User.objects.create_user(username="test", password="testpass")
        self.create_url = reverse('app-create')
        self.login_url = reverse('login')

    def test_smoke(self) -> None:
        login_payload = {
            'username': 'test',
            'password': 'testpass'
        }
        login_response = self.client.post(self.login_url, data=login_payload, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        self.assertIn('token', login_response.data)

        token = login_response.data['token']
        
        create_payload = {
            'title': 'Test App',
            'description': 'A sample test app',
            'price': '9.99'
        }
        headers = {
            "Authorization": f"Token {token}"
        }
        create_response = self.client.post(self.create_url, data=create_payload, format='json', headers=headers)
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(App.objects.count(), 1)

        app_instance = App.objects.first()
        self.assertIsNotNone(app_instance)
        self.assertEqual(app_instance.owner, self.test_user)
        self.assertFalse(app_instance.is_verified)

        site = AdminSite()
        app_admin = AppAdmin(App, site)
        queryset = App.objects.filter(id=app_instance.id)
        verify_apps(app_admin, None, queryset)
        app_instance.refresh_from_db()
        self.assertTrue(app_instance.is_verified)

        
