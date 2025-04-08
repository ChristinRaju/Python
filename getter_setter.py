class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    @property # Getter method
    def balance(self):
        return self.__balance

    @balance.setter # Setter method
    def balance(self, amount):
        if amount < 0:
            print("Cannot set a negative balance.")
        else:
            self.__balance = amount
            print(f"Balance successfully set to ₹{self.__balance}")

# Usage
acc = BankAccount(10000)
print(f"Initial balance: ₹{acc.balance}")

acc.balance =  15000 #Setting a new balance
print(f"Updated balance: ₹{acc.balance}")
