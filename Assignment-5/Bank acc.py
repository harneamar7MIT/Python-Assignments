
# Create Bank Account History System.

class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid Deposit Amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}. New balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Account Balance: ₹{self.balance}")

# Enter Account Details.

print("Account Summary: ")
account = BankAccount(8025, 273)
account.deposit(660)
account.withdraw(160)
account.check_balance()