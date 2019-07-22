import requests
from api import *


class Polygon:
    def __init__(self, api_key, staging=False):
        self._api_key = get_api_key()
        self._api_key = api_key
        self._staging = staging
        self._session = requests.Session()

    def _request(self, method, path, params=None, version='v1'):
        url = 'https://api.polygon.io/' + version + path
        params = params or {}
        params['apiKey'] = self._api_key
        if self._staging:
            params['staging'] = 'true'
        resp = self._session.request(method, url, params=params)
        resp.raise_for_status()
        return resp.json()

    def get(self, path, params=None, version='v1'):
        return self._request('GET', path, params=params, version=version)

    def grouped_daily(self, date, locale="US", market="STOCKS", unadjusted="false"):
        path = '/aggs/grouped/locale/{}/market/{}/{}?unadjusted={}'.format(locale, market, date, unadjusted)
        raw = self.get(path, version='v2')
        return raw
