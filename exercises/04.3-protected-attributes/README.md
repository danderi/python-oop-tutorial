# Protected Attributes and Naming Conventions

## 📝 Instructions

1. Create a class called `LibraryItem` in `app.py` that demonstrates the use of protected attributes:
   - Protected attribute `_title` for the item's title
   - Protected attribute `_author` for the item's author
   - Protected attribute `_available` for availability status
   - Public methods to access and modify these attributes
   - A protected method `_update_availability()`

2. Create a derived class `Book` that inherits from `LibraryItem`:
   - Adds a protected attribute `_isbn`
   - Uses the parent's protected attributes appropriately
   - Implements a public method `display_info()` that shows all information
   - Demonstrates proper use of protected members from parent class

## 💡 Hints

- Use single underscore (`_`) for protected attributes
- Protected attributes are accessible in derived classes
- Protected methods should only be called by other methods in the same class or derived classes
- Document the intended access level in docstrings

## Why Protected vs Private?

Protected attributes in Python:
1. Are accessible from derived classes (unlike private)
2. Indicate "internal use" through convention
3. Are useful for inheritance-based designs
4. Allow more flexibility than private attributes

## Expected Output
```python
book = Book("Python Programming", "John Smith", "123-456-789")
print(book.display_info())
# Should print: "Book: Python Programming by John Smith (ISBN: 123-456-789) - Available: True"

book.check_out()
print(book.display_info())
# Should print: "Book: Python Programming by John Smith (ISBN: 123-456-789) - Available: False"
```
