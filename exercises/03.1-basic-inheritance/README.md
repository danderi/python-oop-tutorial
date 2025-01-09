# Basic Inheritance Exercise

## 📝 Instructions

1. Create a base class called `Animal` in `app.py` with:
   - An `__init__` method that takes `name` and `species` as parameters
   - A method called `make_sound()` that prints "Some generic sound"

2. Create a derived class called `Dog` that inherits from `Animal`:
   - Override the `make_sound()` method to print "Woof!"
   - Add a new method called `fetch()` that prints "{name} is fetching the ball"

## 💡 Hints

- Use the `class ChildClass(ParentClass):` syntax for inheritance
- Remember to call the parent's `__init__` using `super().__init__()`
- Override methods by defining them with the same name in the child class

## Expected Output
When running test code:
```python
dog = Dog("Buddy", "Canine")
dog.make_sound()  # Should print: "Woof!"
dog.fetch()       # Should print: "Buddy is fetching the ball"
```
