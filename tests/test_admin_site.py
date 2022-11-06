from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

LOGIN_URL = reverse("admin:login")
ADMIN_INDEX_URL = reverse("admin:index")
USERS_CHANGELIST_URL = reverse("admin:auth_user_changelist")


class TestAdminSite(TestCase):
    def assert_response_status_code(self, url: str, expected_status_code: int):
        response = self.client.get(url)
        self.assertEqual(expected_status_code, response.status_code)

    def test_anonymous_admin_access(self):
        self.assert_response_status_code(LOGIN_URL, HTTPStatus.NOT_FOUND)
        self.assert_response_status_code(ADMIN_INDEX_URL, HTTPStatus.NOT_FOUND)
        self.assert_response_status_code(USERS_CHANGELIST_URL, HTTPStatus.NOT_FOUND)

    def test_authenticated_admin_access(self):
        user = User.objects.create_user(username="user")
        self.client.force_login(user)

        self.assert_response_status_code(LOGIN_URL, HTTPStatus.NOT_FOUND)
        self.assert_response_status_code(ADMIN_INDEX_URL, HTTPStatus.NOT_FOUND)
        self.assert_response_status_code(USERS_CHANGELIST_URL, HTTPStatus.NOT_FOUND)

    def test_authorized_admin_access(self):
        user = User.objects.create_superuser(username="super", password="secret", email="super@example.com")
        self.client.force_login(user)

        self.assert_response_status_code(LOGIN_URL, HTTPStatus.NOT_FOUND)
        self.assert_response_status_code(ADMIN_INDEX_URL, HTTPStatus.OK)
        self.assert_response_status_code(USERS_CHANGELIST_URL, HTTPStatus.OK)
