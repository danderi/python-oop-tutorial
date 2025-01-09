# Basic Encapsulation with Private Attributes

## 📝 Instructions

1. Create a class called `BankAccount` in `app.py` with:
   - A private attribute `__balance` initialized in `__init__` with a starting balance
   - A private attribute `__account_number` set in `__init__`
   - A method `get_balance()` that returns the current balance
   - A method `deposit(amount)` that adds to the balance
   - A method `withdraw(amount)` that subtracts from the balance if sufficient funds exist
   - A method `display_info()` that returns account info as a string

2. The `withdraw` method should:
   - Check if there are sufficient funds
   - Return True and update balance if successful
   - Return False if insufficient funds

## 💡 Hints

- Use double underscores (`__`) to make attributes private
- Private attributes can still be accessed within class methods
- Try to access `__balance` directly from outside the class - it won't work!

## Expected Output
```python
account = BankAccount(1000, "1234")
print(account.get_balance())  # Should print: 1000
print(account.deposit(500))   # Should print: True
print(account.withdraw(2000)) # Should print: False
print(account.withdraw(800))  # Should print: True
print(account.get_balance())  # Should print: 700
```
