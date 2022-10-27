import json
import time
import redis

from .commands import Message
from .yourfirm import yourfirm_search
from .models import Subscription
from django.conf import settings

redis_duplicate_checker = redis.StrictRedis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB
)


class Crawler:
    # We will only check first page of the results,
    # Hopefully we run this job enough time in a day to don't lose any job
    @classmethod
    def crawl(cls):
        subscriptions = Subscription.objects.all()

        for subscription in subscriptions:
            cached_jobs = redis_duplicate_checker.get(subscription.term)
            if not cached_jobs:
                cached_jobs = yourfirm_search(subscription.term)['result']
                redis_duplicate_checker.set(
                    subscription.term,
                    json.dumps(cached_jobs),
                    ex=settings.YOURFIRM_RESPONSE_CACHE_TIME
                )
            else:
                cached_jobs = json.loads(cached_jobs)
            jobs = sorted(cached_jobs, key=lambda x: x['id'])
            for job in jobs:
                try:
                    job_id = int(job['id'])
                except Exception:
                    continue
                if job_id > subscription.last_sent_job:
                    message_text = (
                        f"New Job:\n\n*{job['name']}*\n\nhttps://www.yourfirm.de{job['url']}"
                    )
                    message = Message(subscription.profile.user_id, message_text)
                    message.send_response()
                    subscription.last_sent_job = job_id
                    subscription.save()
                    time.sleep(1)
