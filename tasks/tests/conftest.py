#テストファイルを補助する役割があるファイル
import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def user(db):
    return User.objects.create_user("testuser", password="pass")


@pytest.fixture
def other_user(db):
    return User.objects.create_user("otheruser", password="pass")


@pytest.fixture
def api_client(user, api_client_factory):
    return api_client_factory(user=user)


@pytest.fixture
def unauthenticated_client():
    return APIClient()


@pytest.fixture
def api_client_factory():
    def factory(user=None, token=None):
        client = APIClient()

        if user:
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)

        if token:
            client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

        return client

    return factory
