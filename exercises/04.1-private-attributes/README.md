# Let's Build a Secure Bank Account! 🏦

We are going to create a `BankAccount` class that keeps your money safe, just like a real bank!

This exercise is perfect for learning about private attributes because:
- We want to keep the balance protected
- Only special methods should change the money
- We need to ensure that no one can mess things up accidentally

## 📝 Instructions

1. **Define a `BankAccount` class** that should:
   - Keep your account balance private `balance` (this means the balance should not be directly accessible from outside the class).
   - Store a unique account number, which should also be private `account_number`.
   - Provide a `get_balance` method that allows you to check your balance safely. This method should return the account balance.
   - Allow deposits through a `deposit` method, which increases the balance when money is deposited.
   - Allow withdrawals through a `withdraw` method, but only if the balance is sufficient. If you don't have enough money, the withdrawal should be denied.
   - Have a `display_info` method that shows the account information, including the account number and the current balance in a clear and readable manner. Example: `"Account {self.__account_number}: Balance = ${self.__balance}"`.

2. The withdrawal system should:
   - First check if you have enough money to make the withdrawal.
   - Only allow the withdrawal if the amount is less than or equal to the current balance.
   - Keep proper track of the balance after each withdrawal operation.

3. **Test your solution.** Create an instance of the `BankAccount` class called `account` with:

```bash
initial_balance: 1000
account_number: "1234"
```

4. Perform some operations by executing methods such as: get the balance, deposit 500, withdraw 2000, then try to withdraw 800 and get your balance again.

5. Print only the result of your `.display_info()` method.

Think of it like using an ATM: you can check your balance, put money in, and take money out, but only if you follow the correct steps. Just like a real bank keeps your money safe! 🏦

### 💡 Tips:
- Attributes like the balance (`balance`) and the account number (`account_number`) should be private, so they cannot be modified directly from outside the class. This is done by placing two underscores `__` before their names (e.g., `__balance`).
- Make sure the `deposit` method only accepts positive amounts.
- The `withdraw` method should be able to deny withdrawals if the requested amount is greater than the available balance.
- Try accessing `__balance` directly - it won't work (that's good!)

This is how professional programmers keep their code safe and organized. You are learning real-world programming skills! 🌟
