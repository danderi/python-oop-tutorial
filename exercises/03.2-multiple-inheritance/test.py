import unittest
from unittest.mock import patch
from app import Flying, Swimming, Bird, Duck

class TestDuck(unittest.TestCase):
    @patch('builtins.print')
    def test_duck_introduce(self, mock_print):
        duck = Duck("Donald", "Mallard")
        duck.introduce()
        mock_print.assert_called_once_with("I'm Donald, a Mallard that can both fly and swim!")

    @patch('builtins.print')
    def test_duck_fly(self, mock_print):
        duck = Duck("Donald", "Mallard")
        duck.fly()
        mock_print.assert_called_once_with("I can fly!")

    @patch('builtins.print')
    def test_duck_swim(self, mock_print):
        duck = Duck("Donald", "Mallard")
        duck.swim()
        mock_print.assert_called_once_with("I can swim!")

if __name__ == "__main__":
    unittest.main()