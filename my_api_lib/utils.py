from .client import APIClient

class BankingAPI(APIClient):
    def get_accounts(self, city):
        return self.get("/accounts")
