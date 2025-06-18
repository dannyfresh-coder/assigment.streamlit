from account import Account


class SavingsAccount(Account):
    def __init__(self, balance, interest_rate=0.03):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

    def get_balance(self):
        return self.balance
