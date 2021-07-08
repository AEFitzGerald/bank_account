
class BankAccount:
    #class attributes
    bank_name = "Ada Ventures"
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        
        return self
    
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient funds: charging a $5 fee")
            self.balance -= 5
            
        return self
        
    def display_account_info(self):
        print(self.balance)
        
        return self
    
    def yield_interest(self):
        self.balance += self.balance*self.int_rate
            
        return self
    
    @staticmethod
    def can_withdraw(balance, amount):
        if(balance - amount) < 0:
            return False
        else:
            return True
        
        
    def all_balances (cls):
        sum = 0      
        
        for account in cls.all_accounts:
            sum += account.balance
        return sum   

account554 = BankAccount(.03, 3000)
account623 = BankAccount(.03, 5000)

account554.deposit(4000).deposit(2500).deposit(9800).withdraw(1100).yield_interest().display_account_info()

account623.deposit(11000).deposit(130500).withdraw(80000).withdraw(25000).yield_interest().display_account_info()
    


#get class method to print all instances of bank accounts

# #class method to change the name of the bank

# @classmethod
# def change_bank_name(cls,name):
#     cls.bank_name = name 

# #class method to get balance of all accounts   
# @classmethod 