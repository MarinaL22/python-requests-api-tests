import requests
from config.config import BASE_URL

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL

    def get(self, path, **kwargs):
        return requests.get(f"{self.base_url}{path}", **kwargs)

    def post(self, path, json=None, **kwargs):
        return requests.post(f"{self.base_url}{path}", json=json, **kwargs)

    def put(self, path, json=None, **kwargs):
        return requests.put(f"{self.base_url}{path}", json=json, **kwargs)

    def delete(self, path, **kwargs):
        return requests.delete(f"{self.base_url}{path}", **kwargs)