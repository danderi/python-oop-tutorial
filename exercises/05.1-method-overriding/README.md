# Let's Make Different Shapes Do Math Their Own Way! 📐

We are going to create different shapes that can calculate their areas and perimeters in unique and special ways.

In this exercise, the shapes (circle, rectangle, triangle) share common methods (area, perimeter, and describe), but each implements these actions uniquely according to their properties.

## 📝 Instructions

1. Create the base class `Shape`. This class will act as a template for other shapes, it doesn't have specific details, just basic methods that you can use or override later.

2. Add these methods to `Shape`:
   - **area:** This method will always return 0. For now, it doesn't calculate anything.
   - **perimeter:** Same as area, this method will return 0.
   - **describe:** This method will simply return the text `Generic shape`.

3. Create a class called `Circle`. This class needs an attribute `radius`, which will be the size of the circle. Example:

```python
class Circle(Shape):
   def __init__(self, radius):
      self.radius = radius
   
   def area(self):
      return 0
   
   def perimeter(self):
      return 0
   
   def describe(self):
      return "Generic shape"
```

4. Just like we did in the previous step, create the class `Rectangle`. This class needs the attributes `width` and `height`, which will be the dimensions of the rectangle.

5. Create the class `Triangle`. This class needs the attributes `side1`, `side2`, `side3` (the three sides of the triangle) and `height` (the height to calculate the area).

6. **Overridden methods.** Override the methods `area`, `perimeter`, and `describe` and implement the specific formulas to calculate area and perimeter, and adjust the describe method for each shape.

- `area`: Calculate the area according to the specific formulas of the shape (for example, for a circle it is π*r² which translated to programming language would be `pi * self.radius ** 2`).
- `perimeter`: Calculate the perimeter according to the shape.
- `describe`: Return a custom description for each shape.

7. **Test your code**. Create a circle, a rectangle, and a triangle using the classes you just made.
Verify that the methods work correctly by calling them. For example:

```python
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5, 4)

print(circle.area())  # Approximately 78.54
print(rectangle.area())  # 24
print(triangle.area())  # 6

print(circle.describe())    # Shows "Circle with radius 5 - Area: 78.54, Perimeter: 31.42"
print(rectangle.describe()) # Shows "Rectangle 4x6 - Area: 24, Perimeter: 20"
print(triangle.describe())  # Shows "Triangle with sides 3,4,5 - Area: 6, Perimeter: 12"
```

## 💡 Hint

Here are the formulas you will need:
- Area of the circle = πr² (π ≈ 3.14159)
- Perimeter of the circle = 2πr
- Area of the rectangle = width × height
- Perimeter of the rectangle = 2(width + height)
- Area of the triangle = ½ × base × height
- Perimeter of the triangle = sum of the three sides
