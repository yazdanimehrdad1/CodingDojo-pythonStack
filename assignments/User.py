class User:
    def __init__(self,name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance+=amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance-= amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self
    def transfer_money(self, other_user, amount):
        self.make_withdrawl(amount)
        other_user.account_balance +=amount
        return self

user1 = User("Mike", "mike@gmail.com")
user2 = User("Antony", "antony@gmail.com")

user1.make_deposit(100).make_deposit(500).display_user_balance()
user2.display_user_balance()
user1.transfer_money(user2, 50).display_user_balance()
user2.display_user_balance()

