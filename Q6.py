'''
6)Question BankAccount creation
'''

class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


class MinimumBalanceAccount(BankAccount):
    def __init__(self):
        BankAccount.__init__(self)
        self.minimum_balance = 1000

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount)
        return self.balance
a = BankAccount()
b = MinimumBalanceAccount()
a.deposit(10000)
print(a.deposit(1000))
b.deposit(1000000)
print(b.withdraw(10))

