# Building an Intelligent Library System! 📚

We are going to create a library system where books can be shared between different parts of our program, but in a safe and organized way! The goal of this exercise is to learn about protected attributes in Python while building a basic library management system.

This exercise is perfect for learning about protected attributes because:
- Some information needs to be shared (like book titles)
- We want to be careful about how it is used
- It's like having "staff only" areas in a library!

## 📝 Instructions

1. Create a class called `LibraryItem`. This will be the "model" for all objects in our library (books, magazines, etc.)

2. Add some attributes inside the constructor. In the `__init__` method of the `LibraryItem` class, add protected attributes:
   - `_title`: title of the item, which will be text.
   - `_author`: author of the item, also text.
   - `_is_available`: indicates if the item is available. It will always start as True (i.e., available).

   ```python
      class LibraryItem:
         def __init__(self, title, author):
            self._title = title
            self._author = author
            self._is_available = True
   ```

3. Create a protected method called `_update_availability` that updates the availability status of the item. This method will change the availability status of the items. Think of it as the one responsible for marking something as "borrowed" or "available".

   ```python
   def _update_availability(self, is_available):
       self._is_available = is_available
   ```

4. Define a public method `check_out`. This method will handle borrowing the item:

   - If the item is available, change it to "not available" using `_update_availability`.
   - If it is already borrowed, print a message like:

   ```python
   "{title} not available"
   ```

5. Define another public method `return_item`. This will mark the item as available again (as if someone returned the book).

6. Create a class `Book` that inherits from `LibraryItem` and add a protected attribute `_isbn` in the constructor to store the book's ISBN number.

   ```python
   def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self._isbn = isbn
   ```

7. Implement a public method called `display_info` that shows all the information of the book (title, author, availability, and ISBN) in an orderly manner. Example:

   ```python
   "Book: {title} by {author} (ISBN: {isbn}) - Available: {available}"
   ```

8. **Test your solution.** Create an instance of the `Book` class called `book` with fictitious data:

   ```python
   book = Book("Harry Potter", "J.K. Rowling", "123456789")
   ```

   - Use `display_info` to show the book's information.
   - Use `check_out` to borrow the book and show the information again with `display_info`.
   - Use `return_item` to return the book and verify that everything works correctly.


## 💡 Tips

- Use `_` (underscore) for protected attributes and methods.
- "Protected" means "be careful when interacting with this".
- Child classes can access the protected attributes and methods of their parent class.
- Choose clear names to indicate what should be treated as protected.
