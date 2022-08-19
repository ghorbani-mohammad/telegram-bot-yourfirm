from .commands import Message
from .yourfirm import Yourfirm
from .models import Subscription


class Crawler:
    def crawl(self):
        subscriptions = Subscription.objects.all()

        for subscription in subscriptions:
            jobs = Yourfirm.search(subscription.term)['result']
            jobs = sorted(jobs, key=lambda x: int(x['id']))
            for job in jobs:
                job_id = int(job['id'])
                if job_id > (subscription.last_sent_job or 0):
                    message = Message(subscription.profile.user_id, job['name'])
                    message.send_response()
                    subscription.last_sent_job = job_id
                    subscription.save()
