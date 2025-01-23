class BankAccount:
    def __init__(self, initial_balance, account_number):
        self.__balance = initial_balance
        self.__account_number = account_number
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def display_info(self):
        return f"Account {self.__account_number}: Balance = ${self.__balance}"

# Test code
if __name__ == "__main__":
    account = BankAccount(1000, "1234")
    account.get_balance()  # 1000
    account.deposit(500)   # True
    account.withdraw(2000) # False
    account.withdraw(800)  # True
    account.get_balance()  # 700
    print(account.display_info())
