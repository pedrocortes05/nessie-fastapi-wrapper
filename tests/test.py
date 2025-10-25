import pytest
from dotenv import load_dotenv
from my_api_lib.client import APIClient

load_dotenv()
api_Key = os.getenv("API_KEY")

def test_get(monkeypatch):
    class MockResponse:
        def json(self): return {"status": "ok"}
        def raise_for_status(self): pass
    def mock_get(*args, **kwargs): return MockResponse()
    monkeypatch.setattr("requests.get", mock_get)

    client = APIClient("http://api.nessieisreal.com", api_Key)
    response = client.get("/accounts")
    assert response["status"] == "ok"
