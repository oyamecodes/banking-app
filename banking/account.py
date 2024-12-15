class Account:
    def __init__(self, account_id, name, initial_balance=0):
        self.account_id = account_id
        self.name = name
        self.balance = initial_balance
        self.transactions = []

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append((amount, 'deposit'))
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append((-amount, 'withdraw'))
        return self.balance

    def get_transactions(self):
        return self.transactions