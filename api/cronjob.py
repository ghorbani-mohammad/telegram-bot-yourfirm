from .commands import Message
from .yourfirm import Yourfirm
from .models import Subscription


class Crawler:
    # We will only check first page of the results,
    # Hopefully we run this job enough time in a day to don't lose any job
    def crawl(self):
        subscriptions = Subscription.objects.all()

        for subscription in subscriptions:
            jobs = Yourfirm.search(subscription.term)['result']
            jobs = sorted(jobs, key=lambda x: int(x['id']))
            for job in jobs:
                job_id = int(job['id'])
                if job_id > subscription.last_sent_job:
                    message = Message(subscription.profile.user_id, job['name'])
                    message.send_response()
                    subscription.last_sent_job = job_id
                    subscription.save()
