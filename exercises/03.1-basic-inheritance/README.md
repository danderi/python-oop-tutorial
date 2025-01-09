# Let's Create a Pet Family! 🐾

Hey! Remember how we talked about inheritance being like a family tree? Now we're going to create our own programming family with animals!

## Why Are We Making This? 🐕

Think about pets:
- All animals can make sounds and have names
- But dogs are special - they can fetch things!
- This is perfect for learning how inheritance works

We'll create:
1. A basic `Animal` class (like a parent)
2. A special `Dog` class (like a child) that can do everything an animal can do, plus more!

## What We'll Learn 📚

- How to create a basic class that other classes can inherit from
- How to make a new class that builds on the basic one
- How to add special abilities to our new class
- How to use features from the parent class

## 📝 Your Task

1. Create a base class called `Animal` that:
   - Takes a name and species when created
   - Can make a basic sound

2. Create a `Dog` class that:
   - Is a special type of Animal
   - Makes a "Woof!" sound instead of the basic animal sound
   - Can fetch things!

## 💡 Need Help?

- Use `class Dog(Animal):` to say that Dog is a type of Animal
- Use `super().__init__()` to set up the Animal part of your Dog
- When a dog makes a sound, it should override (replace) the animal sound
- Add a new `fetch()` method that only dogs have

## What Should Happen? 🎯

When you run this code:
```python
dog = Dog("Buddy", "Canine")
dog.make_sound()  # Should print: "Woof!"
dog.fetch()       # Should print: "Buddy is fetching the ball"
```

Think of it like this: Just like how you can do everything your parents can do (like walk and talk) plus your own special things, a Dog can do everything an Animal can do plus its own special tricks! 🌟