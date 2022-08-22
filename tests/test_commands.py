import pytest

from django.urls import reverse
from django.conf import settings


@pytest.mark.django_db
def test_subscribe(client):
    url = reverse('api:push_data')
    r = client.post(
        url,
        {
            'message': {
                'chat': {
                    'id': settings.TEST_ACCOUNT_ID,
                },
                'text': '/subscribe php',
            }
        },
        content_type="application/json",
    )
    assert r.status_code == 200


@pytest.mark.django_db
def test_unsubscribe(client):
    url = reverse('api:push_data')
    r = client.post(
        url,
        {
            'message': {
                'chat': {
                    'id': settings.TEST_ACCOUNT_ID,
                },
                'text': '/unsubscribe php',
            }
        },
        content_type="application/json",
    )
    assert r.status_code == 200
