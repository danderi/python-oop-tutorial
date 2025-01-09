# Multiple Inheritance in Python

## 📝 Instructions

1. Create three base classes in `app.py`:
   - `Flying` with a method `fly()` that prints "I can fly!"
   - `Swimming` with a method `swim()` that prints "I can swim!"
   - `Bird` with attributes `name` and `species`

2. Create a class called `Duck` that inherits from all three classes:
   - Initialize it with `name` and `species`
   - Add a method `introduce()` that prints "I'm {name}, a {species} that can both fly and swim!"

## 💡 Hints

- Use multiple inheritance by listing all parent classes: `class Duck(Bird, Flying, Swimming):`
- The order of inheritance matters (Method Resolution Order - MRO)
- Use `super().__init__()` to properly initialize the parent classes

## Expected Output
When running test code:
```python
duck = Duck("Donald", "Mallard")
duck.introduce()  # Should print: "I'm Donald, a Mallard that can both fly and swim!"
duck.fly()        # Should print: "I can fly!"
duck.swim()       # Should print: "I can swim!"
```
