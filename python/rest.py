import requests
import json


class Rest:

    def __init__(self, url: str = None):
        self.url = url

    def ping(self, url: str = None):
        url = self.validate_url(url)
        res = requests.get(url)
        return res.text

    def validate_url(self, url: str = None) -> str:
        if self.url is None and url is None:
            raise Exception("URL not provided")
        if url is None:
            return self.url
        return url
