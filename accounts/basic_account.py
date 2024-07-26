# Creating BasicAccount class that is a parent to other account classes
class BasicAccount:
    bank = "Fio Banka"
    accountType = "Basic account"

    def __init__(self, owner):

        self.owner = owner
        self.balance = 0

    # Defining insert balance method
    def insert_balance(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Your {self.accountType} has been credited with {amount} dollars.")
        else:
            print("Invalid amount. Please enter a positive value.")

    # Defining withdraw balance method
    def withdraw_balance(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Your {self.accountType} has been debited with {amount} dollars.")
        elif amount > self.balance:
            print("Insufficient funds. Please enter a smaller amount.")
        else:
            print("Invalid amount. Please enter a positive value.")

    # Overwriting default __str__ method
    def __str__(self):
        return (
            "\nPrinting account information:\n"
            f"  Account owner name: {self.owner}\n"
            f"  Your bank is: {self.bank}\n"
            f"  Your account type is: {self.accountType}\n"
            f"  Your disposable balance is {self.balance} dollars.\n"
        )
