class User:

   def __init__(self, interest, balance=20000):
        self.interest = interest
        self.balance = balance

   def make_deposit(self, amount):
    	self.account_balance += amount
        return self

   def make_withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self

   def display_account_info(self):
        return self.balance
