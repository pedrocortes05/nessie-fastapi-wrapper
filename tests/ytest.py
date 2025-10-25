import os
from my_api_lib.client import APIClient

apiKey = os.getenv("API_KEY")

def test_get():
    client = APIClient("http://api.nessieisreal.com", apiKey)
    response = client.get("/accounts")
    assert response["status"] == "ok"

test_get()