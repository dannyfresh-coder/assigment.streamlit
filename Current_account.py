from account import Account


class CurrentAccount(Account):
    def __init__(self, balance, overdraft_limit=0):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def get_balance(self):
        return self.balance
