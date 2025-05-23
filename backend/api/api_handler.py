import requests
from abc import ABC, abstractmethod

class APIHandler(ABC):
    def __init__(self, base_url, auth_type=None, headers=None, **auth_kwargs):
        self.base_url = base_url
        self.auth_type = auth_type
        self.auth_headers = headers or {}
        self.auth_kwargs = auth_kwargs
        self.token = None

        if auth_type == "oauth2":
            self.token = self.get_oauth_token()
            self.auth_headers["Authorization"] = f"Bearer {self.token}"
        elif auth_type == "api_key":
            self.auth_headers.update(auth_kwargs.get("headers", {}))

    @abstractmethod
    def get_oauth_token(self):
        """Implement with Subclasses"""
        pass

    def get(self, endpoint:str, params=None):
        url:str = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.auth_headers, params=params)
        self._check_response(response)
        return response.json()

    def post(self, endpoint:str, data=None, json=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.auth_headers, data=data, json=json)
        self._check_response(response)
        return response.json()

    def _check_response(self, response):
        if response.status_code == 401 and self.auth_type == "oauth2":
            self.token = self.get_oauth_token()
            self.auth_headers["Authorization"] = f"Bearer {self.token}"
        response.raise_for_status()
