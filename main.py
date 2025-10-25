from dotenv import load_dotenv
import os

from my_api_lib.utils import BankingAPI
from tests.ytest import test_get

load_dotenv()
api_Key = os.getenv("API_KEY")

client = BankingAPI("http://api.nessieisreal.com", api_Key)
response = client.get_accounts()

print(response)