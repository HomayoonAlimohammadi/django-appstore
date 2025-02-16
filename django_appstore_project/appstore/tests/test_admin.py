from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from appstore.models import App

User = get_user_model()

class AdminFilterTest(TestCase):
    """
    Test suite for the Django admin filtering based on the is_verified status.
    """

    def setUp(self) -> None:
        """
        Create an admin user and sample App instances with different verification statuses.
        """
        self.client: Client = Client()
        self.admin_user = User.objects.create_superuser(
            username='admin', password='adminpass', email='admin@example.com'
        )
        self.client.force_login(self.admin_user)

        self.user = User.objects.create_user(
            username='user', password='userpass', email='user@example.com'
        )
        self.verified_app: App = App.objects.create(
            title='Verified App',
            description='A verified application',
            price='1.99',
            owner=self.user,
            is_verified=True
        )
        self.unverified_app: App = App.objects.create(
            title='Unverified App',
            description='An unverified application',
            price='2.99',
            owner=self.user,
            is_verified=False
        )

    def test_admin_filter_by_verified_status(self) -> None:
        """
        Test that filtering in the admin change list returns the correct apps based on the verification status.
        """
        url = reverse('admin:appstore_app_changelist')

        response = self.client.get(url, {'is_verified__exact': '1'})
        self.assertContains(response, 'Verified App')
        self.assertNotContains(response, 'Unverified App')

        response = self.client.get(url, {'is_verified__exact': '0'})
        self.assertContains(response, 'Unverified App')
        self.assertNotContains(response, 'Verified App')
