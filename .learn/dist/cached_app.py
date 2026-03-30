from math import pi

class Shape:
    """Base class for all shapes"""
    def area(self):
        """Calculate the area of the shape"""
        return 0
    
    def perimeter(self):
        """Calculate the perimeter of the shape"""
        return 0
    
    def describe(self):
        """Return a description of the shape"""
        return "Generic shape"

# Create your Circle class here
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi * self.radius
    
    def describe(self):
        return f"Circle with radius {self.radius} - Area: {self.area()}, Perimeter: {self.perimeter()}"

# Create your Rectangle class here
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def describe(self):
        return f"Rectangle {self.width}x{self.height} - Area: {self.area()}, Perimeter: {self.perimeter()}"

# Create your Triangle class here
class Triangle(Shape):
    def __init__(self, side1, side2, side3, height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.height = height
    
    def area(self):
        return (self.side1 * self.height) / 2
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def describe(self):
        return f"Triangle with sides {self.side1},{self.side2},{self.side3} - Area: {self.area()}, Perimeter: {self.perimeter()}"