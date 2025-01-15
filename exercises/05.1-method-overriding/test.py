import unittest
from math import pi
from app import Shape, Circle, Rectangle, Triangle

class TestShapes(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(5)
        self.rectangle = Rectangle(4, 6)
        self.triangle = Triangle(3, 4, 5, 4)

    def test_circle_area(self):
        self.assertAlmostEqual(self.circle.area(), pi * 5 ** 2, places=2)

    def test_rectangle_area(self):
        self.assertEqual(self.rectangle.area(), 24)

    def test_triangle_area(self):
        self.assertEqual(self.triangle.area(), 6)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(self.circle.perimeter(), 2 * pi * 5, places=2)

    def test_rectangle_perimeter(self):
        self.assertEqual(self.rectangle.perimeter(), 20)

    def test_triangle_perimeter(self):
        self.assertEqual(self.triangle.perimeter(), 12)

    def test_circle_describe(self):
        self.assertEqual(self.circle.describe(), "Circle with radius 5 - Area: 78.54, Perimeter: 31.42")

    def test_rectangle_describe(self):
        self.assertEqual(self.rectangle.describe(), "Rectangle 4x6 - Area: 24, Perimeter: 20")

    def test_triangle_describe(self):
        self.assertEqual(self.triangle.describe(), "Triangle with sides 3,4,5 - Area: 6, Perimeter: 12")

if __name__ == "__main__":
    unittest.main()