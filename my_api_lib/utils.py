from .client import APIClient

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
