import requests

class APIClient:
    def __init__(self, base_url, api_key=None, timeout=10):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.timeout = timeout

    def _headers(self):
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    def append_api_key(self, url):
        if not self.api_key:
            return url

        if '?' in url:
            # Already has parameters
            return url + f"&key={self.api_key}"
        else:
            return url + f"?key={self.api_key}"

    def get(self, endpoint, params=None):
        """Send a GET request to the API."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        url = self.append_api_key(url)
            
        response = requests.get(url, headers=self._headers(), params=params, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None):
        """Send a POST request to the API."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        url = self.append_api_key(url)

        response = requests.post(url, headers=self._headers(), json=data, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, data=None):
        """Send a POST request to the API."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        url = self.append_api_key(url)

        response = requests.put(url, headers=self._headers(), json=data, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint):
        """Send a POST request to the API."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        url = self.append_api_key(url)
        print(f"{url=}")

        response = requests.delete(url, headers=self._headers(), timeout=self.timeout)
        response.raise_for_status()

        if response.status_code == 204 or not response.text.strip():
            return {"status": "success", "message": "Deleted successfully"}
        
        return response
