class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
kobe = User("Kobe Bryant", "kobe@python.com")

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawl(400).display_user_balance()

monty.make_deposit(50).make_deposit(150).make_withdrawl(25).make_withdrawl(15).display_user_balance()

kobe.make_deposit(500).make_withdrawl(50).make_withdrawl(50).make_withdrawl(50).display_user_balance()

guido.transfer_money(monty, 100)
