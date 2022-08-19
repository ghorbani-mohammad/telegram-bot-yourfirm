import requests


class Yourfirm():
    BASE_URL = 'https://www.yourfirm.de'

    @classmethod
    def search(cls, term):
        url = f'{Yourfirm.BASE_URL}/api/jobs/?name={term}'
        r = requests.get(url)
        return r.json()
