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