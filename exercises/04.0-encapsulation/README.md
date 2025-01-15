# Keeping Our Code Safe and Organized! 🔒

In this section, we will learn about something called **encapsulation**. Although it sounds complicated, it's like having a safe for your data!

Let's see what it means in programming.

## What is it about? 📦

Imagine you have a piggy bank:

- You can put money through the slot (this is like adding information to the class).
- You can use a code to get the amount of money inside (this would be querying the information in a controlled way).
- But you can't directly grab the money inside the piggy bank because it's protected!

That's what encapsulation does in programming: it organizes and "protects" the data so it doesn't get modified incorrectly.

## Why do we need this? 🤔

Think about your phone:
- You don't need to know how it works inside to use it.
- The operating system and functions are protected inside the casing, and you only interact with what is allowed.

Similarly, encapsulation helps us:
- Keep our code safe and avoid accidental errors.
- Change how something works without affecting other parts of the code.
- Keep the code organized and easy to understand.

## The Important Parts 🎯

1. **Making Data Private**
   - Sometimes, we need the data of a class to be private, meaning only the class itself can modify it.
   - In Python, we use `__` before names to do this, like `__balance` in a piggy bank.
   - This helps us avoid other parts of the program from accidentally changing this data.

2. **Protected Data**
   - Other data can be "protected," meaning it is available for other parts of the program to use, but only with caution.
   - We use `_` before the name for these attributes, like `_secure_code`.
   - They are more accessible than private data, but we still give them some protection to avoid uncontrolled access.

3. **Safe Access to Data**
   - We create *special methods* to access and modify private or protected data safely.
   - It's like having a cashier instead of being able to open the safe yourself. The cashier allows you to access what you need without risking damage to the system.

Here is an example of encapsulation in Python:

![oop-image-4.0](../../.learn/assets/opp-image-40.png)

In this case, the attribute **__balance** is private and can only be modified through the deposit method. No one can change it directly from outside the class.

## The Special Way of Python 🐍

In Python, it's important to know that encapsulation doesn't completely "block" the data, but it helps us organize and restrict access responsibly.

1. We use `__` and `_` as warning signals not to access certain attributes directly.
2. While Python doesn't prevent us from accessing these attributes, it's good practice to follow these conventions to make our code safer and more organized.

Now, in the next exercises, we will practice these ideas with fun examples. We will do it step by step! 🌟
