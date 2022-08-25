import requests
import urllib.parse as up

from django.conf import settings


class Yourfirm():

    @staticmethod
    def search(term):
        term = up.quote(term, safe='')
        url = f'{settings.YOURFIRM_URL}/api/jobs/?name={term}'
        r = requests.get(url)
        return r.json()
