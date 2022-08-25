import requests
import urllib.parse

from django.conf import settings


def yourfirm_search(term):
    term = urllib.parse.quote(term, safe='')
    url = f'{settings.YOURFIRM_URL}/api/jobs/?name={term}'
    r = requests.get(url)
    return r.json()
