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
    print(account.get_balance())  # 1000
    print(account.deposit(500))   # True
    print(account.withdraw(2000)) # False
    print(account.withdraw(800))  # True
    print(account.get_balance())  # 700
