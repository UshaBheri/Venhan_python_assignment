class BankAccount:
    def __init__(self,account_number,account_holder,balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        self.amount = amount
        self.balance += self.amount

    def withdraw(self,amount):
        self.amount = amount
        if self.balance >= self.amount:
            self.balance -= self.amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance
    
bankDetails = BankAccount('123456789','Usha')

bankDetails.deposit(100.0)
print(bankDetails.get_balance())

bankDetails.withdraw(50.0)
print(bankDetails.get_balance()) # output: 100.0
                                        #  50.0


