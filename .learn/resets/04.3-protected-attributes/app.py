# Create LibraryItem and Book classes here
class LibraryItem:
    """Base class for library items demonstrating protected attributes"""
    def __init__(self, title, author):
        # Initialize protected attributes here
        pass

    def _update_availability(self):
        # Protected method to update availability
        pass

    def check_out(self):
        # Public method to check out the item
        pass

    def return_item(self):
        # Public method to return the item
        pass


class Book(LibraryItem):
    """Derived class demonstrating use of protected attributes from parent"""
    def __init__(self, title, author, isbn):
        # Initialize book with base class attributes plus ISBN
        pass

    def display_info(self):
        # Display all book information
        pass
        
