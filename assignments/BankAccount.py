

class BankAccount:
    def __init__(self, int_rate=0.0, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance+= amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance = self.balance +self.balance*self.int_rate
        return self
    def display_account(self):
        print(self.balance)
        return self


class User:
    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account()
        return self
    def transfer_money(self, other_user, amount):
        self.make_withdrawl(amount)
        other_user.account.balance +=amount
        return self

account1 = BankAccount(0.01, 0)
account2 = BankAccount(0.05, 0)

account1.deposit(100).deposit(400).deposit(100).withdraw(100).yield_interest().display_account()
account2.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account()