class Account():
    def __init__(self, owner, balance):
        self.balance = balance
        self.owner = owner

    def __str__(self):
        return f"Account onwer: {self.owner}, \nAccount balance: {self.balance}$"

    def deposit(self, deposit):
        self.deposit = deposit
        print("Deposit Accepted")
        print(f"Added {deposit}$ to the balance")
        self.balance = self.balance + deposit

    def withdraw(self, withdraw):
        self.withdraw = withdraw
        if(withdraw > self.balance):
            print("Sorry not enough funds!")
        else:
            print("Withdrawal accepted")
            print(f"Added {deposit}$ to the balance")
            self.balance = self.balance - withdraw

acct1 = Account("Lidan", 100)
print(acct1)
acct1.deposit(300)
print((acct1))
acct1.withdraw(500)
print((acct1))