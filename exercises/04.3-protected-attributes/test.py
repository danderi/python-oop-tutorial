import pytest
from io import StringIO
from unittest.mock import patch
from app import Book



@pytest.mark.it("Should create a Book instance and display correct information")
def test_book_creation():
    book = Book("1984", "George Orwell", "9780451524935")
    assert book._title == "1984", "Title should be '1984'"
    assert book._author == "George Orwell", "Author should be 'George Orwell'"
    assert book._isbn == "9780451524935", "ISBN should be '9780451524935'"
    assert book._is_available is True, "Book should be available by default"

@pytest.mark.it("Should lend a book and update its availability")
def test_lend_item():
    book = Book("1984", "George Orwell", "9780451524935")
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        book.lend_item()
        output = mock_stdout.getvalue().strip()
        assert output == "'1984' has been lent out.", "Expected a message indicating the book was lent"
        assert book._is_available is False, "Book should not be available after being lent"

@pytest.mark.it("Should not lend a book if it is already lent")
def test_lend_item_already_lent():
    book = Book("1984", "George Orwell", "9780451524935")
    book.lend_item()  # Lend the book first
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        book.lend_item()
        output = mock_stdout.getvalue().strip()
        assert output == "'1984' is already lent out.", "Expected a message indicating the book is already lent"
        assert book._is_available is False, "Book should still not be available"

@pytest.mark.it("Should return a book and update its availability")
def test_return_item():
    book = Book("1984", "George Orwell", "9780451524935")
    book.lend_item()  # Lend the book first
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        book.return_item()
        output = mock_stdout.getvalue().strip()
        assert output == "'1984' has been returned.", "Expected a message indicating the book was returned"
        assert book._is_available is True, "Book should be available after being returned"
