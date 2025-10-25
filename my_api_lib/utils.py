from .client import APIClient

allowed_data_types = ["Accounts", "Bills", "Customers", "Deposits", "Loans", "Purchases", "Transfers", "Withdrawals"]

class BankingAPI(APIClient):
    # Acccount
    def get_accounts(self):
        return self.get("/accounts")

    def get_account(self, id):
        return self.get(f"/accounts/{id}")

    def get_customer_accounts(self, id):
        return self.get(f"/customers/{id}/accounts")

    def create_account(self, id, body):
        return self.post(f"/customers/{id}/accounts", body)

    def update_account(self, id, body):
        return self.put(f"/accounts/{id}", body)

    def delete_account(self, id):
        return self.delete(f"/accounts/{id}")
    
    # ATM
    def get_atms(self):
        return self.get("/atms")

    def get_atm(self, id):
        return self.get(f"/atms/{id}")

    # Bill
    def get_account_bills(self, id):
        return self.get(f"/accounts/{id}/bills")

    def get_bill(self, bill_id):
        return self.get(f"/bills/{bill_id}")

    def get_customer_bills(self, id):
        return self.get(f"/customers/{id}/bills")
    
    def create_bill(self, id, body):
        return self.post(f"/customers/{id}/bills", body)

    def update_bill(self, bill_id, body):
        return self.put(f"/bills/{bill_id}", body)

    def delete_account(self, bill_id):
        return self.delete(f"/bills/{bill_id}")

    # Branch
    def get_branches(self):
        return self.get("/branches")

    def get_branch(self, id):
        return self.get(f"/branches/{id}")

    # Customer
    def get_account_customer(self, id):
        return self.get(f"/accounts/{id}/customer")

    def get_customers(self):
        return self.get(f"/customers")

    def get_customer(self, id):
        return self.get(f"/customers/{id}")
    
    def create_customer(self, body):
        return self.post(f"/customers", body)

    def update_customer(self, id, body):
        return self.put(f"/customers/{id}", body)

    # Data
    def delete_data(self, data_type=None):
        if not data_type:
            return self.delete("/data")
        elif data_type in allowed_data_types:
            return self.delete(f"/data?type={data_type}")
        else:
            print("Invalid type")
            return

    # Deposit
    def get_account_deposits(self, id):
        return self.get(f"/accounts/{id}/deposits")

    def get_deposit(self, id):
        return self.get(f"/deposits/{id}")

    def create_account_deposit(self, id, body):
        return self.post(f"/accounts/{id}/deposits", body)

    def update_deposit(self, id, body):
        return self.put(f"/deposits/{id}", body)

    def delete_deposit(self, id):
        return self.delete(f"/deposits/{id}")

    # Loan
    def get_account_loans(self, id):
        return self.get(f"/accounts/{id}/loans")

    def get_loan(self, id):
        return self.get(f"/loans/{id}")

    def create_account_loan(self, id, body):
        return self.post(f"/accounts/{id}/loans", body)

    def update_loan(self, id, body):
        return self.put(f"/loans/{id}", body)

    def delete_loan(self, id):
        return self.delete(f"/loans/{id}")

    # Merchant
    def get_merchants(self):
        return self.get(f"/merchants")

    def get_merchant(self, id):
        return self.get(f"/merchants/{id}")

    def create_merchant(self, body):
        return self.post(f"/merchants", body)

    def update_merchant(self, id, body):
        return self.put(f"/merchants", body)

    # Loan
    def get_account_purchases(self, id):
        return self.get(f"/accounts/{id}/purchases")

    def get_merchant_account_purchases(self, id, account_id):
        return self.get(f"/merchants/{id}/accounts/{account_id}/purchases")

    def get_merchant_purchases(self, id):
        return self.get(f"/merchants/{id}/purchases")

    def get_purchase(self, id):
        return self.get(f"/loans/{id}")

    def create_account_purchase(self, id, body):
        return self.post(f"/accounts/{id}/purchases", body)

    def update_purchase(self, id, body):
        return self.put(f"/purchases/{id}", body)

    def delete_purchase(self, id):
        return self.delete(f"/purchases/{id}")

    # Transfer
    def get_account_transfers(self, id):
        return self.get(f"/accounts/{id}/transfers")

    def get_transfer(self, id):
        return self.get(f"/transfers/{id}")

    def create_account_transfer(self, id, body):
        return self.post(f"/accounts/{id}/transfers", body)

    def update_transfer(self, id, body):
        return self.put(f"/transfers/{id}", body)

    def delete_transfer(self, id):
        return self.delete(f"/transfers/{id}")

    # Withdrawal
    def get_account_withdrawals(self, id):
        return self.get(f"/accounts/{id}/withdrawals")

    def get_withdrawal(self, id):
        return self.get(f"/withdrawals/{id}")

    def create_account_withdrawal(self, id, body):
        return self.post(f"/accounts/{id}/withdrawals", body)

    def update_withdrawal(self, id, body):
        return self.put(f"/withdrawals/{id}", body)

    def delete_withdrawal(self, id):
        return self.delete(f"/withdrawals/{id}")