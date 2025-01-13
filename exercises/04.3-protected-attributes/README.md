# Building an Intelligent Library System! 📚

We are going to create a library system where books can be shared between different parts of our program, but in a safe and organized way! The goal of this exercise is to learn about protected attributes in Python while building a basic library management system.

This exercise is perfect for learning about protected attributes because:
- Some information needs to be shared (like book titles)
- We want to be careful about how it is used
- It's like having "staff only" areas in a library!

## 📝 Instructions

1. Create a class called `LibraryItem`.

2. In the constructor (`__init__`), add protected attributes:
   - `_title`: title of the item (string).
   - `_author`: author of the item (string).
   - `_is_available`: availability status (boolean, starts as `True`).

3. Create a protected method called `_update_availability` that updates the availability status of the item.

```python
   def _update_availability(self, is_available):
       self._is_available = is_available
```

4. Define a public method `lend_item` that checks if the item is available. If it is available, update the status to "not available" using `_update_availability`. If it is not available, print a message indicating that it is already lent out.

5. Define another public method `return_item` that marks the item as available.

6. Create a class `Book` that inherits from `LibraryItem` and adds a protected attribute `_isbn` in the constructor to store the book's ISBN number.

```python
   def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self._isbn = isbn
```

7. Implement a public method called `display_info` that shows all the information of the book (title, author, availability, and ISBN) in an organized manner. Example: `Book: {title} by {author} (ISBN: {isbn}) - Available: {available}`

8. **Test your solution.** Create an instance of the `Book` class called `book` with information such as title, author, and ISBN. Call the methods `lend_item` and `return_item` to verify that they work correctly. Use the `display_info` method to display the book's information at each step.

## 💡 Tips

- Use `_` (underscore) for protected things
- Protected means "please be careful with this"
- Child classes can use protected things from their parent
- Use clear names to show what should be protected
