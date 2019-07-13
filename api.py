import requests
import json


class ColeApi:
    def __init__(self, url, key, secret, version):
        self.url = url
        self.key = key
        self.secret = secret
        self.version = version

    def get_historical_data(self):
        requests.get("https://api.polygon.io/v1/last/stocks/AAPL?apiKey=AKBHEJ0EK9IO98U9DB8K")