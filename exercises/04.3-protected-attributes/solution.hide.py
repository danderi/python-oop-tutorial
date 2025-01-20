class LibraryItem:
    """Base class for library items demonstrating protected attributes"""
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._is_available = True
    
    def _update_availability(self, is_available):
        """Protected method to update item availability"""
        self._is_available = is_available
    
    def check_out(self):
        """Public method to check out the item"""
        if self._is_available:
            self._update_availability(False)
            print(f"'{self._title}' has been lent out.")
        else:
            print(f"'{self._title}' is already lent out.")

    
    def return_item(self):
        """Public method to return the item"""
        self._update_availability(True)
        print(f"'{self._title}' has been returned.")


class Book(LibraryItem):
    """Derived class demonstrating use of protected attributes from parent"""
    def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self._isbn = isbn
    
    def display_info(self):
        """Display all book information including protected attributes"""
        return f"Book: {self._title} by {self._author} (ISBN: {self._isbn}) - Available: {self._is_available}"


# Test code
if __name__ == "__main__":
    book = Book("Python Programming", "John Smith", "123-456-789")
    print(book.display_info())
    book.check_out()
    print(book.display_info())
    book.return_item()
    print(book.display_info())
