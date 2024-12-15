'''
Design a Python class for a Bank Account.
The constructor should take parameters for the account holder's name and initial balance. 
Implement private attributes for these parameters. 
Create methods to deposit and withdraw money from the account, as well as to display the account's balance.

Instantiate more than one object from the class, and show suitable testing.
'''

class BankAccount:
    #Instantiate objects
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
    
    def get_balance(self):
        return self._balance
    
    #Adds a positive deposit to the balance
    def deposit(self, deposit):
        if deposit < 0:
            print("Invalid value")
        else:
            self._balance = self._balance + deposit
    
    #Subtracts a positive withdraw value from the balance
    def withdraw(self, withdraw):
        if withdraw < 0:
            print("Invalid value")
        else:
            self._balance = self._balance - withdraw

