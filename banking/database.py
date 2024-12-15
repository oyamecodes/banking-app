from account import Account

class Database:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, name, initial_balance=0):
        if account_id in self.accounts:
            raise ValueError("Account ID already exists")
        self.accounts[account_id] = Account(account_id, name, initial_balance)
        return self.accounts[account_id]

    def get_account(self, account_id):
        if account_id not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[account_id]