from ucty.basic_account import BasicAccount


# Creating Saving account that inherits from BasicAccount
class SavingAccount(BasicAccount):
    accountType = "Saving account"

    def __init__(self, owner, interest):
        super().__init__(owner)
        self.interest = interest

    # Modified BasicAccount insert method
    def insert_balance(self, amount):
        return super().insert_balance(amount + amount * self.interest / 100)

    # Modified BasicAccount withdraw method
    def withdraw_balance(self, amount):
        if amount > self.balance * 0.2:
            print("You cant withdraw more than 20% of the current balance")
        else:
            return super().withdraw_balance(amount)

    # Modified BasicAccount __str__ method
    def __str__(self):
        return (
            super().__str__()
            + f"  Your interest is {self.interest}% and maximum withdraw amount is 20% of your current balance\n"
        )
