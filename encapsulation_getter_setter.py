class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.__balance}")

# Using the class
account = BankAccount("1234567890", 1000)
account.display_info()

account.deposit(500)
account.withdraw(300)
print("Final Balance:", account.get_balance())

# Attempt to access private variable directly (will fail)
# print(account.__balance)  # Uncommenting this will cause an AttributeError
