'''
Create a Python class for a Bank.
Implement a constructor that initializes an empty list to store bank accounts. 
Create methods to add a new account to the bank, find an account by account number, deposit money into an account, withdraw money from an account, and display all accounts' information. 
Instantiate more than one object from the class, and show suitable testing.  
'''

#an object for one bank account
class BankAccount:
    #Instantiate objects
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def display_account_details(self):
        print(f"Account number: {self.account_number} \nName: {self.name} \nBalance: {self.balance}")
        

    #Adds a positive deposit to the balance
    def deposit(self, deposit):
        if deposit < 0:
            print("Invalid value")
        else:
            self.balance = self.balance + deposit
    
    #Subtracts a positive withdraw value from the balance
    def withdraw(self, withdraw):
        if withdraw < 0 or withdraw > self.balance:
            print("Invalid value")
        else:
            self.balance = self.balance - withdraw

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, BankAccount):
        self.accounts.append(BankAccount)

    def find_account(self, account_number):
        valid = False
        counter = 0
        while valid != True and counter != len(self.accounts):
            if self.accounts[counter].account_number == account_number:
                valid = True
            else:
                counter += 1
        if valid == True:
            self.accounts[counter].display_account_details()
        else:
            print("Account does not exist")
    
    def display_accounts(self):
        for i in range(len(self.accounts)):
            self.accounts[i].display_account_details()
            print("\n")



account1 = BankAccount(101, "Alice", 500)
account2 = BankAccount(102, "Bob", 1000)

bank = Bank()
# Adding accounts
bank.add_account(account1)
bank.add_account(account2)

bank.find_account(102)
'''
Outputs -> Account number: 102
Name: Bob
Balance: 1000
'''

bank.find_account(103)
'''
Outputs -> Account does not exist
'''

bank.display_accounts()
'''
Outputs -> Account number: 101
Name: Alice
Balance: 500


Account number: 102
Name: Bob
Balance: 1000


'''