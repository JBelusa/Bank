from accounts.basic_account import BasicAccount


# Creating Junior account that inherits from BasicAccount
class JuniorAccount(BasicAccount):
    accountType = "Junior account"
    withdraw_count = 0
    withdrawn_amount = 0

    def __init__(self, owner, max_withdraw):
        super().__init__(owner)
        self.max_withdraw = max_withdraw

    # Modified BasicAccount withdraw method
    def withdraw_balance(self, amount):

        if self.withdrawn_amount + amount > self.max_withdraw:
            print("You can't withdraw more than specified maximum amount")
            return
        if self.withdraw_count >= 4:
            print("You've reached maximum withdrawal count (4).")
            return

        self.withdraw_count += 1
        self.withdrawn_amount += amount
        return super().withdraw_balance(amount)

    # Modified BasicAccount __str__ method
    def __str__(self):
        return (
            super().__str__()
            + f"  Your maximum withdraw amount is {self.max_withdraw} and you have withdrawn {self.withdraw_count}x times\n"
        )
