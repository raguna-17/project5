import pytest
from rest_framework.test import APIClient
from tasks.models import Task

pytestmark = pytest.mark.django_db


def test_unauthenticated_access(unauthenticated_client):
    res = unauthenticated_client.get('/tasks/api/tasks/')
    assert res.status_code == 401


def test_invalid_token(api_client_factory):
    client = api_client_factory(token="invalid")
    res = client.get('/tasks/api/tasks/')
    assert res.status_code in (401, 403)


def test_other_user_cannot_access(api_client, other_user):
    task = Task.objects.create(title='x', user=other_user)
    res = api_client.get(f'/tasks/api/tasks/{task.id}/')
    assert res.status_code in (403, 404)


def test_other_user_cannot_modify(api_client, other_user):
    task = Task.objects.create(title='x', user=other_user)
    res = api_client.patch(f'/tasks/api/tasks/{task.id}/toggle/')
    assert res.status_code in (403, 404)

def test_authenticated_user_can_list(api_client, user):
    Task.objects.create(title="ok", user=user)
    res = api_client.get('/tasks/api/tasks/')
    assert res.status_code == 200
    assert len(res.data) == 1
