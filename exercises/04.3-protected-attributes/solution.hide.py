class LibraryItem:
    """Base class for library items demonstrating protected attributes"""
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._available = True
    
    def _update_availability(self, status):
        """Protected method to update item availability"""
        self._available = status
    
    def check_out(self):
        """Public method to check out the item"""
        if self._available:
            self._update_availability(False)
            return True
        return False
    
    def return_item(self):
        """Public method to return the item"""
        if not self._available:
            self._update_availability(True)
            return True
        return False


class Book(LibraryItem):
    """Derived class demonstrating use of protected attributes from parent"""
    def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self._isbn = isbn
    
    def display_info(self):
        """Display all book information including protected attributes"""
        return f"Book: {self._title} by {self._author} (ISBN: {self._isbn}) - Available: {self._available}"


# Test code
if __name__ == "__main__":
    book = Book("Python Programming", "John Smith", "123-456-789")
    print(book.display_info())
    book.check_out()
    print(book.display_info())
    book.return_item()
    print(book.display_info())
