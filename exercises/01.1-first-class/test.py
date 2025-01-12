import unittest
from unittest.mock import patch
from app import Person

class TestPerson(unittest.TestCase):
    @patch('builtins.print')
    def test_greet(self, mock_print):
        person = Person("John")
        person.greet()
        mock_print.assert_called_once_with("Hello, my name is John")

if __name__ == "__main__":
    unittest.main()




# import unittest
# from solution import Person

# class TestPerson(unittest.TestCase):
#     def test_greet(self):
#         person = Person("John")
#         self.assertEqual(person.greet(), "Hello, my name is John")

# if __name__ == "__main__":
#     unittest.main()