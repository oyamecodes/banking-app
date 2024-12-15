class Transaction:
    @staticmethod
    def transfer(sender, receiver, amount):
        if sender.withdraw(amount):
            receiver.deposit(amount)
            return True
        return False