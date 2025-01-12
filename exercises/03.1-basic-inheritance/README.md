# Creating a Pet Family! 🐾

Let's create our own programming family with animals. In this exercise, you will learn about inheritance in programming by creating a base class and a derived class. This will help you understand how classes can share and extend functionalities.

## 📝 Instructions

1. Define a base class called `Animal`.

2. In its `__init__` method, define the following attributes: name, species.

3. Add a method called `make_sound` that prints a generic sound like: `"Some generic sound"`.

4. Define a class `Dog` that inherits from `Animal`.

```python
class Dog(Animal):
   pass
```

5. Override the `make_sound` method in the `Dog` class to print `"Woof!"` instead of the generic sound.

6. Add a method called `fetch` to the `Dog` class that prints a message like `"<name> is fetching the ball"`.

7. **Test your solution.** Create an instance of the `Dog` class called `my_dog` with:

```bash
name: "Buddy"
species: "Canine"
```

8. Call the `make_sound` and `fetch` methods on `my_dog`.

You should see on the screen:

```bash
Woof!
Buddy is fetching the ball
```