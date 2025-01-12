# Creating Your First Class - Let's Start Simple 🚀

Hello! Today we're going to learn how to create a "class" in Python. If you've never heard of this before, don't worry! Here's a simple explanation:

- A class is like a **mold** or a **template**.
- For example, if we wanted to describe "people," we could create a mold called `Person`. This mold could define that every person has a name and can greet others.

Let's create our own mold called `Person` so Python can use it!

---

## 📝 Instructions

1. **Create the mold.** Write this in your `app.py` file:

```python
class Person:
    pass
```

Now you have a basic class called `Person`. It doesn’t do anything yet, but it exists.


2. **Add basic information (a name).** We want every person to have a name. For that, we use something special called `__init__`. This is a method that sets up our person when we create it:


```python
class Persona:
    def __init__(self, name):
        self.name = name
```

--
- `__init__` is executed automatically when we create a person.
- `self.name` stores the name so that we can use it later.

--

3. **Make our person greet**. Now we want the class to do something. We will add a method called `greet` that will print a message:

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def greet(self):
        print(f"Hello, my name is {self.name}")
```

--

- `greet` is an action that our class can perform.
- It uses the name we stored with `self.name` to personalize the greeting.

4. **Use your class.** Write the following code below your class in `app.py` and run it:

```python
   person = Person("John")
   person.greet()
```

You should see in the terminal:

```
Hello, my name is John
```