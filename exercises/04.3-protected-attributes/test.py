import unittest
from app import LibraryItem, Book

class TestLibraryItem(unittest.TestCase):
    def setUp(self):
        self.book = Book("Python Programming", "John Smith", "123-456-789")

    def test_initial_availability(self):
        self.assertTrue(self.book._available)

    def test_check_out(self):
        self.assertTrue(self.book.check_out())
        self.assertFalse(self.book._available)

    def test_return_item(self):
        self.book.check_out()
        self.assertTrue(self.book.return_item())
        self.assertTrue(self.book._available)

    def test_display_info(self):
        expected_info = "Book: Python Programming by John Smith (ISBN: 123-456-789) - Available: True"
        self.assertEqual(self.book.display_info(), expected_info)
        self.book.check_out()
        expected_info = "Book: Python Programming by John Smith (ISBN: 123-456-789) - Available: False"
        self.assertEqual(self.book.display_info(), expected_info)

if __name__ == "__main__":
    unittest.main()