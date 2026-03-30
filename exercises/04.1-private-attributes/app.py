# Create your BankAccount class here
class BankAccount:
    def __init__(self, balance, account_number):
        self.__balance = balance
        self.__account_number = account_number
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, money_deposited):
        self.__balance += money_deposited

    
    def withdraw(self, money_to_withdraw):
        if money_to_withdraw <= self.__balance :
            self.__balance-= money_to_withdraw
 

    def display_info(self):
        print(f'Account {self.__account_number}: Balance = ${self.__balance}')


account = BankAccount(1000, "1234")
