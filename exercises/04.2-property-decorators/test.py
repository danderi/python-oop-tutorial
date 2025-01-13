import unittest
from app import Temperature

class TestTemperature(unittest.TestCase):
    def setUp(self):
        self.temp = Temperature(25)

    def test_initial_celsius(self):
        self.assertEqual(self.temp.celsius, 25)

    def test_initial_fahrenheit(self):
        self.assertEqual(self.temp.fahrenheit, 77.0)

    def test_set_celsius(self):
        self.temp.celsius = 100
        self.assertEqual(self.temp.celsius, 100)
        self.assertEqual(self.temp.fahrenheit, 212.0)

    def test_set_fahrenheit(self):
        self.temp.fahrenheit = 32
        self.assertEqual(self.temp.celsius, 0)
        self.assertEqual(self.temp.fahrenheit, 32)

    def test_invalid_celsius(self):
        with self.assertRaises(ValueError):
            self.temp.celsius = -300

if __name__ == "__main__":
    unittest.main()