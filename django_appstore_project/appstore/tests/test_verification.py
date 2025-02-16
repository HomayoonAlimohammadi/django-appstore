from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.admin.sites import AdminSite

from ..models import App
from ..admin import AppAdmin, verify_apps

User = get_user_model()


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
        verify_apps(app_admin, None, queryset)
        self.app1.refresh_from_db()
        self.app2.refresh_from_db()
        self.assertTrue(self.app1.is_verified)
        self.assertTrue(self.app2.is_verified)

