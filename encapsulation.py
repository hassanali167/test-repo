"""
Topic: Encapsulation in Python

Explanation:
Encapsulation restricts direct access to class attributes and methods.
Private attributes use a double underscore (`__`).
"""

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited {amount}, New Balance: {self.__balance}"

    def get_balance(self):
        return self.__balance  # Accessing private variable via method

# Creating an object
account = BankAccount(1000)

print(account.deposit(500))
print("Balance:", account.get_balance())

"""
Code Explanation:
- `__balance` is a private variable.
- Methods `deposit()` and `get_balance()` allow controlled access.
- Direct access to `__balance` is not allowed.
"""
