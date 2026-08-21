# Implement a class representing an account exception,
# Implement a class representing a single bank account,
# This class should control access to the account number 
# and account balance attributes by implementing the properties:

# 1. it should be possible to read the account number only, not change it. 
# In case someone tries to change the account number, raise an alarm by 
# raising an exception;
# 2.it should not be possible to set a negative balance. In case
# someone tries to set a negative balance, raise an alarm by raising 
# an exception;
# 3. when the bank operation (deposit or withdrawal) is above 100.000, 
# then additional message should be printed on the standard output 
# (screen) for auditing purposes;
# 4. it should not be possible to delete an account as long as 
# the balance is not zero;

class AccountException(Exception):
    pass

class Account():
    def __init__(self, accountNumber):
        self.__accountNumber = accountNumber
        self.__balance = 0

    @property
    def accountNumber(self):
        return self.__accountNumber

    @accountNumber.setter
    def accountNumber(self, amount):
        raise AccountException

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise AccountException
        else:
            self.__balance = amount

    @balance.deleter
    def balance(self):
        if self.__balance > 0:
            print("Cannot delete account that contains money!")
        self.__balance = None
    
    def withdraw(self, amount):
        if amount < 0:
            raise AccountException
        if self.__balance - amount < 0:
            raise AccountException
        else:
            if amount > 100000:
                print("NOTICE, ACCOUNT IS TRYING TO WITHDRAW OVER 100K")
            self.__balance -= amount
            print(f"{amount}$ has been withdrawn from the account")
            print(f"Balance: {self.__balance}")

    def deposit(self, amount):
        if amount < 0:
            raise AccountException
        if amount > 100000:
            print("NOTICE, ACCOUNT IS TRYING TO DEPOSIT OVER 100K")
        self.__balance += amount
        print(f"{amount} has been deposited to the account")
        print(f"Balance: {self.__balance}")
        





# setting the balance to 1000;
account = Account(6969)
account.balance = 1000

# trying to set the balance to -200;
try:
    account.balance = -200
except AccountException:
    print("Cannot set account balance to negative")

# trying to set a new value for the account number;
try:
    account.accountNumber = 50
except AccountException:
    print("Cannot change the account number")

# trying to deposit 1.000.000;
account.deposit(1000000)

# trying to delete the account attribute containing a non-zero balance.
try:
    del account.balance
except AccountException:
    print("Cannot delete an account: it contains money!")