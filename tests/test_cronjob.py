import pytest

from api.cronjob import Crawler
from django.conf import settings
from api.models import Profile, Subscription


@pytest.mark.django_db
def test_subscribe(client):
    profile = Profile.objects.create(user_id=settings.TEST_ACCOUNT_ID)
    Subscription.objects.create(profile=profile, term='python')
    Crawler.crawl()
