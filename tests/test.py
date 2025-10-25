import pytest
from my_api_lib.client import APIClient

apiKey = os.getenv("API_KEY")

def test_get(monkeypatch):
    class MockResponse:
        def json(self): return {"status": "ok"}
        def raise_for_status(self): pass
    def mock_get(*args, **kwargs): return MockResponse()
    monkeypatch.setattr("requests.get", mock_get)

    client = APIClient("http://api.nessieisreal.com", apiKey)
    response = client.get("/accounts")
    assert response["status"] == "ok"
