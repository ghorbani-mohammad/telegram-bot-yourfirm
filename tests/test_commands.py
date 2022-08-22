import pytest

from django.urls import reverse
from django.conf import settings

from api.models import Profile, Subscription


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
    profiles_count = Profile.objects.count()
    subscriptions_count = Subscription.objects.count()
    conditions = (profiles_count == 1) and (subscriptions_count == 1)
    assert r.status_code == 200 and conditions


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
    profiles_count = Profile.objects.count()
    subscriptions_count = Subscription.objects.count()
    conditions = (profiles_count == 1) and (subscriptions_count == 0)
    assert r.status_code == 200 and conditions
