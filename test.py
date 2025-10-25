from dotenv import load_dotenv
import os

from my_api_lib.utils import BankingAPI

load_dotenv()
api_Key = os.getenv("API_KEY")


client = BankingAPI("http://api.nessieisreal.com", api_Key)

awa = {
  "first_name": "Pedro",
  "last_name": "Cortes",
  "address": {
    "street_number": "123",
    "street_name": "Street",
    "city": "San Pedro",
    "state": "NL",
    "zip": "10100"
  }
}
response = client.create_customer(awa)
print(response)

response = client.get_customers()
print(response)

first_customer = response[0]
response = client.get_customer(first_customer['_id'])
print(response)

awa = {
    "address": {
        "street_number": "234"
    }
}

response = client.update_customer(first_customer['_id'], awa)
print(response)

response = client.get_customer(first_customer['_id'])
print(response)

# response = client.delete_data("Customers")
# print(response)

response = client.get_branches()
print(response)