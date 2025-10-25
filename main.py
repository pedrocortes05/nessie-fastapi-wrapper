from typing import Union, Optional
from fastapi import FastAPI, Body
from dotenv import load_dotenv
import os

from my_api_lib.utils import BankingAPI

load_dotenv()
api_Key = os.getenv("API_KEY")

client = BankingAPI("http://api.nessieisreal.com", api_Key)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Account
@app.get("/accounts")
def get_accounts(data_type: str = None):
    return client.get_accounts()

@app.get("/accounts/{id}")
def get_account(id: int):
    return client.get_account(id)

@app.get("/customers/{id}/accounts")
def get_customer_account(id: int):
    return client.get_customer_accounts(id)

@app.post("/customers/{id}/accounts")
def create_account(id: int, body: dict = Body(...)):
    return client.create_account(id, body)

@app.put("/accounts/{id}")
def update_account(id: int, body: dict = Body(...)):
    return client.update_account(id, body)

@app.delete("/accounts/{id}")
def delete_account(id: int):
    return client.delete_account(id)

# ATM
@app.get("/atms")
def get_atms(lat: str = None, lng: str = None, rad: str = None):
    return client.get_atms()

@app.get("/atms/{atm_id}")
def get_atm(atm_id: int):
    return client.get_atm(atm_id)

# Bill
@app.get("/accounts/{id}/bills")
def get_account_bills(id: int):
    return client.get_account_bills(id)

@app.get("/bills/{bill_id}")
def get_bill(bill_id: int):
    return client.get_bill(id)

@app.get("/customers/{id}/bills")
def get_customer_bills(id: int):
    return client.get_customer_bills(id)

@app.post("/customers/{id}/bills")
def create_bill(id: int, body: dict = Body(...)):
    return client.create_bill(id, body)

@app.put("/bills/{bill_id}")
def update_bill(bill_id: int, body: dict = Body(...)):
    return client.update_bill(id, body)

@app.delete("/bills/{bill_id}")
def delete_bill(bill_id: int):
    return client.delete_bill(id)

# Branch
@app.get("/branches")
def get_branches():
    return client.get_branches()

@app.get("/branches/{id}")
def get_branch(id: int):
    return client.get_branch(id)

# Customer
@app.get("/accounts/{id}/customer")
def get_account_customer(id: int):
    return client.get_account_customer(id)

@app.get("/customers")
def get_customers():
    return client.get_customers()

@app.get("/customers/{id}")
def get_customer(id: int):
    return client.get_customer(id)

@app.post("/customers")
def create_customer(body: dict = Body(...)):
    return client.create_customer(body)

@app.put("/customers/{id}")
def update_customer(id: int, body: dict = Body(...)):
    return client.update_customer(id, body)

# Data
@app.delete("/data")
def delete_data(data_type: str = None):
    return client.delete_data(data_type)

# Deposit
@app.get("/accounts/{id}/deposits")
def get_account_deposits(id: int):
    return client.get_account_deposits(id)

@app.get("/deposits/{id}")
def get_deposit(id: int):
    return client.get_deposit(id)

@app.post("/accounts/{id}/deposits")
def create_account_deposit(id: int, body: dict = Body(...)):
    return client.create_account_deposit(id, body)

@app.put("/deposits/{id}")
def update_deposit(id: int, body: dict = Body(...)):
    return client.update_deposit(id, body)

@app.delete("/deposits/{id}")
def delete_deposit(id: int):
    return client.delete_deposit(id)

# Loan
@app.get("/accounts/{id}/loans")
def get_account_loans(id: int):
    return client.get_account_loans(id)

@app.get("/loans/{id}")
def get_loan(id: int):
    return client.get_loan(id)

@app.post("/accounts/{id}/loans")
def create_account_loan(id: int, body: dict = Body(...)):
    return client.create_account_loan(id, body)

@app.put("/loans/{id}")
def update_loan(id: int, body: dict = Body(...)):
    return client.update_loan(id, body)

@app.delete("/loans/{id}")
def delete_loan(id: int):
    return client.delete_loan(id)

# Merchant
@app.get("/merchants")
def get_merchants(lat: str = None, lng: str = None, rad: str = None):
    return client.get_merchants()

@app.get("/merchants/{id}")
def get_merchant(id: int):
    return client.get_merchant(id)

@app.post("/merchants")
def create_merchant(body: dict = Body(...)):
    return client.create_merchant(body)

@app.put("/merchants")
def update_merchant(id: int, body: dict = Body(...)):
    return client.update_merchant(id, body)

# Loan
@app.get("/accounts/{id}/purchases")
def get_account_purchases(id: int):
    return client.get_account_purchases(id)

@app.get("/merchants/{id}/accounts/{account_id}/purchases")
def get_merchant_account_purchases(id: int, account_id):
    return client.get_merchant_account_purchases(id, account_id)

@app.get("/merchants/{id}/purchases")
def get_merchant_purchases(id: int):
    return client.get_merchant_purchases(id)

@app.get("/loans/{id}")
def get_purchase(id: int):
    return client.get_purchase(id)

@app.post("/accounts/{id}/purchases")
def create_account_purchase(id: int, body: dict = Body(...)):
    return client.create_account_purchase(id, body)

@app.put("/purchases/{id}")
def update_purchase(id: int, body: dict = Body(...)):
    return client.update_purchase(id, body)

@app.delete("/purchases/{id}")
def delete_purchase(id: int):
    return client.delete_purchase(id)

# Transfer
@app.get("/accounts/{id}/transfers")
def get_account_transfers(id: int, data_type: str = None):
    return client.get_account_transfers(id)

@app.get("/transfers/{id}")
def get_transfer(id: int):
    return client.get_transfer(id)

@app.post("/accounts/{id}/transfers")
def create_account_transfer(id: int, body: dict = Body(...)):
    return client.create_account_transfer(id, body)

@app.put("/transfers/{id}")
def update_transfer(id: int, body: dict = Body(...)):
    return client.update_transfer(id, body)

@app.delete("/transfers/{id}")
def delete_transfer(id: int):
    return client.delete_transfer(id)

# Withdrawal
@app.get("/accounts/{id}/withdrawals")
def get_account_withdrawals(id: int):
    return client.get_account_withdrawals(id)

@app.get("/withdrawals/{id}")
def get_withdrawal(id: int):
    return client.get_withdrawal(id)

@app.post("/accounts/{id}/withdrawals")
def create_account_withdrawal(id: int, body: dict = Body(...)):
    return client.create_account_withdrawal(id, body)

@app.put("/withdrawals/{id}")
def update_withdrawal(id: int, body: dict = Body(...)):
    return client.update_withdrawal(id, body)

@app.delete("/withdrawals/{id}")
def delete_withdrawal(id: int):
    return client.delete_withdrawal(id)