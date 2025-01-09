# Creating Your First Class - Let's Start Simple! 🎨

Hey! Remember when we talked about classes being like blueprints? Well, now we're going to create our very first blueprint! We'll make a simple `Person` class that will help us understand how classes work.

## Why Are We Making This? 🤔

In real life, every person has a name and can say hello to others, right? We're going to create a simple class that does just that! This will help us understand:
- How to create a basic class (our blueprint)
- How to give our class some basic information (like a name)
- How to make our class do something (like say hello)

## What We'll Learn 📚

- How to create a class using the `class` keyword
- How to add information to our class using `__init__` (this is like setting things up when we first create something)
- How to make our class do things using methods (these are like special actions our class can perform)

## 📝 Your Task

1. Open `app.py` and create a class called `Person`
2. Add a special setup method (`__init__`) that takes a person's name
3. Store the name so we can use it later
4. Add a method called `greet` that will make our person say hello

## 💡 Need Help? 

- To create a class, start with `class Person:`
- The `__init__` method is special - it runs when we create a new person
- Use `self.name` to store the name (think of `self` as "myself" - it's how the class refers to itself)
- Your `greet` method should print something like "Hello, my name is (whatever name was given)"

## What Should Happen? 🎯

When someone uses your class like this:
```python
person = Person("Bob")
person.greet()
```

They should see:
```
Hello, my name is Bob
```

Don't worry if it seems tricky at first - we all start somewhere! Give it a try, and remember: coding is like learning a new language, it takes practice! 🌟