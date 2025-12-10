class BankAccount:  # Create Class
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def transfer(self, amount, other_account):
        if amount <= 0:
            print("Transfer amount must be positive.")
            return
        if amount > self.balance:
            print("Sorry, you cannot afford that amount")
        else:
            self.balance -= amount
            other_account.balance += amount
            print(f"Transferred £{amount} to {other_account.owner}. Your balance: £{self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
        else:
            self.balance += amount
            print(f"Deposited £{amount}. New balance: £{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
            return
        if amount > self.balance:
            print("You cannot withdraw more than you have")
        else:
            self.balance -= amount
            print(f"You withdrew £{amount}. New balance: £{self.balance}")

    def display_balance(self):
        print(f"Your balance is £{self.balance}")


# Inherits from BankAccount
class StudentAccount(BankAccount):  # Inheritance
    def __init__(self, owner, balance, student_id):
        super().__init__(owner, balance)
        self.student_id = student_id

    def get_details(self):
        print(f"Student {self.owner} with ID {self.student_id} has balance £{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
            return
        if amount > self.balance:
            print("Students can’t overdraw!")
        else:
            self.balance -= amount
            print(f"Student withdrew £{amount}. Remaining balance: £{self.balance}")


# Encapsulation:
class SecureStudentAccount(StudentAccount):
    def __init__(self, owner, balance, student_id):
        super().__init__(owner, balance, student_id)
        self.__balance = max(0, balance)

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            print(f"Balance updated. New balance: £{self.__balance}")
        else:
            print("Balance cannot be negative.")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
        else:
            self.__balance += amount
            print(f"Deposited £{amount}. New balance: £{self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
            return
        if amount > self.__balance:
            print("You cannot withdraw more than you have")
        else:
            self.__balance -= amount
            print(f"You withdrew £{amount}. New balance: £{self.__balance}")

    def transfer(self, amount, other_account):
        if amount <= 0:
            print("Transfer amount must be positive.")
            return
        if amount > self.__balance:
            print("Sorry, you cannot afford that amount")
        else:
            self.__balance -= amount
            other_account.deposit(amount)  # use other object's public API
            print(f"Transferred £{amount} to {other_account.owner}. Your balance: £{self.__balance}")

    def display_balance(self):
        print(f"Your balance is £{self.__balance}")

    def get_details(self):
        print(f"Secure Student {self.owner} (ID {self.student_id}). Balance: £{self.__balance}")


class PremiumAccount(BankAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
            return
        if self.balance - amount >= -100:
            self.balance -= amount
            print(f"Withdrew £{amount}. New balance: £{self.balance}")
        else:
            print("Overdraft limit reached! ")


