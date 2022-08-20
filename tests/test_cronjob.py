import pytest

from api.cronjob import Crawler
from django.conf import settings
from api.models import Profile, Subscription


@pytest.mark.django_db
def test_subscribe():
    # In this test we have not assertion, Hopefully if we have any error
    # We will get an exception
    profile = Profile.objects.create(user_id=settings.TEST_ACCOUNT_ID)
    Subscription.objects.create(profile=profile, term='python')
    Crawler.crawl()
