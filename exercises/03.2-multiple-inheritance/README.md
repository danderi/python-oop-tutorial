# Multiple Inheritance in Python

## 📝 Instructions

1. Create three base classes in `app.py`:
   - `Flying` with a method `fly()` that prints "I can fly!"
   - `Swimming` with a method `swim()` that prints "I can swim!"
   - `Bird` with attributes `name` and `species`

2. Create a class called `Duck` that inherits from the three classes:
   - In the `__init__` method of `Duck`, use `super().__init__()` to call the constructor of `Bird` as we did in the previous exercise.
   - Define a method `introduce()` that prints: `"I'm {name}, a {species} that can both fly and swim!"`

3. **Test your solution.** Create an instance of the `Duck` class named `duck` with:

```bash
name: "Donald"
species: "Mallard"
```

When running the test code, it should print:

```python
"I'm Donald, a Mallard that can both fly and swim!"
"I can fly!"
"I can swim!"
```

## 💡 Tips

- Use multiple inheritance by listing all parent classes: `class Duck(Bird, Flying, Swimming):`
- The order of inheritance matters (Method Resolution Order - MRO)
- Use `super().__init__()` to properly initialize the parent classes
