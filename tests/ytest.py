import os
from dotenv import load_dotenv
from my_api_lib.client import APIClient

load_dotenv()
api_key = os.getenv("API_KEY")

def test_get():
    client = APIClient("http://api.nessieisreal.com", api_key)
    response = client.get("/customers")
    print(response)
    # assert response["status"] == "ok"
