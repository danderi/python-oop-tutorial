import pytest
from app import LibraryItem, Book 

@pytest.mark.it("Create the LibraryItem class with protected attributes (_title, _author, _is_available)")
def test_libraryitem_creation():
    item = LibraryItem("Generic Title", "Generic Author")
    assert item._title == "Generic Title", "The title attribute was not set correctly."
    assert item._author == "Generic Author", "The author attribute was not set correctly."
    assert item._is_available is True, "The availability attribute should be True by default."

@pytest.mark.it("Implement the _update_availability method in the LibraryItem class")
def test_update_availability():
    item = LibraryItem("Generic Title", "Generic Author")
    item._update_availability(False)
    assert item._is_available is False, "The availability was not updated to False."
    item._update_availability(True)
    assert item._is_available is True, "The availability was not updated to True."


@pytest.mark.it("Create the Book class with an additional ISBN attribute")
def test_book_creation():
    book = Book("Harry Potter", "J.K. Rowling", "123456789")
    assert book._title == "Harry Potter", "The title attribute was not set correctly in the Book class."
    assert book._author == "J.K. Rowling", "The author attribute was not set correctly in the Book class."
    assert book._isbn == "123456789", "The ISBN attribute was not set correctly in the Book class."
    assert book._is_available is True, "The book should be available by default."

@pytest.mark.it("Implement the display_info method in the Book class")
def test_display_info():
    book = Book("Harry Potter", "J.K. Rowling", "123456789")
    expected_output = "Book: Harry Potter by J.K. Rowling (ISBN: 123456789) - Available: True"
    assert book.display_info() == expected_output, "The display_info output is incorrect."

@pytest.mark.it("Test the full flow of the Book class")
def test_book_full_flow():
    book = Book("Harry Potter", "J.K. Rowling", "123456789")
    
    # Check initial availability
    assert book._is_available is True, "The book should be available initially."
    
    # Check out the book
    book.check_out()
    assert book._is_available is False, "The book should be marked as not available after check_out."
    
    # Return the book
    book.return_item()
    assert book._is_available is True, "The book should be marked as available after return_item."


