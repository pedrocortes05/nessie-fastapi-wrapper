import requests
import json
import os

customerId = '1'
apiKey = os.getenv("API_KEY")

# url = f'http://api.reimaginebanking.com/customers/{customerId}/accounts?key={apiKey}'
# payload = {
#   "type": "Savings",
#   "nickname": "test",
#   "rewards": 10000,
#   "balance": 10000,	
# }

url = f'http://api.nessieisreal.com/customers?key={apiKey}'
payload = {
  "first_name": "Pedro",
  "last_name": "Cortes",
  "address": {
    "street_number": "123",
    "street_name": "Dally",
    "city": "San Pedro",
    "state": "NL",
    "zip": "10100"
  }
}

# Create a Savings Account
response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
	print('account created')
else:
    print(f"Failed: {response.status_code}")
    print(response.text)