# Method Overriding with Shape Calculations

## 📝 Instructions

1. Create a base class called `Shape` in `app.py` with:
   - An abstract method `area()` that returns 0
   - An abstract method `perimeter()` that returns 0
   - A method `describe()` that returns a string with the shape's name and its measurements

2. Create three derived classes:
   - `Circle` with radius as parameter
   - `Rectangle` with width and height as parameters
   - `Triangle` with base and height for area, and three sides for perimeter

3. Requirements for each shape:
   - Override `area()` and `perimeter()` with proper calculations
   - Use proper mathematical formulas (π = 3.14159 for circle)
   - Override `describe()` to include shape-specific details

## 💡 Hints

- Use `math.pi` for more accurate circle calculations
- Circle area = πr²
- Circle perimeter = 2πr
- Rectangle area = width × height
- Rectangle perimeter = 2(width + height)
- Triangle area = ½ × base × height
- Triangle perimeter = sum of all sides

## Expected Output
```python
# Creating shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5, 4)  # sides: 3,4,5, height: 4

# Printing areas
print(circle.area())      # Should print: 78.53975
print(rectangle.area())   # Should print: 24
print(triangle.area())    # Should print: 6

# Printing descriptions
print(circle.describe())    # Should print: "Circle with radius 5 - Area: 78.54, Perimeter: 31.42"
print(rectangle.describe()) # Should print: "Rectangle 4x6 - Area: 24, Perimeter: 20"
print(triangle.describe())  # Should print: "Triangle with sides 3,4,5 - Area: 6, Perimeter: 12"
```

## Why This Exercise?

This exercise demonstrates:
1. How different shapes can share a common interface (Shape)
2. How each shape can implement area and perimeter calculations differently
3. How polymorphism allows us to work with different shapes through their common base class
4. Real-world application of method overriding
