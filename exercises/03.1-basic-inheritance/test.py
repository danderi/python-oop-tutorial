import unittest
from unittest.mock import patch
from app import Animal, Dog

class TestAnimalDog(unittest.TestCase):
    @patch('builtins.print')
    def test_animal_make_sound(self, mock_print):
        animal = Animal("Generic Animal", "Unknown")
        animal.make_sound()
        mock_print.assert_called_once_with("Some generic sound")

    @patch('builtins.print')
    def test_dog_make_sound(self, mock_print):
        dog = Dog("Buddy", "Canine")
        dog.make_sound()
        mock_print.assert_called_once_with("Some generic sound")

    @patch('builtins.print')
    def test_dog_fetch(self, mock_print):
        dog = Dog("Buddy", "Canine")
        dog.fetch()
        mock_print.assert_called_once_with("Buddy is fetching the ball")

if __name__ == "__main__":
    unittest.main()