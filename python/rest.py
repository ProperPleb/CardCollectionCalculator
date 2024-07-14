import requests
import json
import logging

from config import Config
from requests import Response


class Rest:

    def __init__(self, url: str = None):
        self.logger = logging.getLogger(__name__)
        self.conf = Config()
        if url is None:
            self.base_url = self.conf.config("host.url")
        else:
            self.base_url = url

    def getGrid(self, request: str, query: str = None) -> Response:
        url = self.urlSetup("host.action.query.prefix", "host.action.query.suffix", query.lower().replace(" ", "+"))
        self.logger.info(url)
        return requests.post(url, json=json.loads(request))

    def getDetailView(self, request: str, product_id: str):
        url = self.urlSetup("host.action.list.prefix", "host.action.list.suffix", product_id)
        return requests.post(url, json=json.loads(request))

    def urlSetup(self, prefix: str, suffix: str, content: str = None):
        pre = self.conf.config(prefix)
        suf = self.conf.config(suffix)
        if content is None:
            content = ""
        return self.base_url + pre + content + suf
