import requests

from django.conf import settings


class Yourfirm():

    @classmethod
    def search(cls, term):
        url = f'{settings.YOURFIRM_URL}/api/jobs/?name={term}'
        r = requests.get(url)
        return r.json()
