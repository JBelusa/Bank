from ucty.basic_account import BasicAccount
from ucty.saving_account import SavingAccount
from ucty.junior_account import JuniorAccount


def print_line():
    print(80 * "-")


print_line()
print("Testing Basic Account")
print_line()
# Testing Basic Account
basic_acc = BasicAccount("Jirka")

print(basic_acc)
basic_acc.insert_balance(500)
basic_acc.withdraw_balance(300)
basic_acc.withdraw_balance(1000)
print(basic_acc)


print_line()
print("Testing Saving Account")
print_line()
# Testing Saving Account
saving_acc = SavingAccount("Franta", 10)

print(saving_acc)
saving_acc.insert_balance(500)
saving_acc.withdraw_balance(100)
saving_acc.withdraw_balance(300)
print(basic_acc)


print_line()
print("Testing Junior Account")
print_line()
# Testing Junior Account
junior_acc = JuniorAccount("Pavel", 100)

print(junior_acc)
junior_acc.insert_balance(500)
i = 0

while i <= 4:
    junior_acc.withdraw_balance(50)
    i += 1
print(junior_acc)
