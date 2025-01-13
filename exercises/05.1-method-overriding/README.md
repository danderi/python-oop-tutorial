# Let's Make Different Shapes Do Math Their Own Way! 📐

We are going to create different shapes that can calculate their areas and perimeters in unique and special ways.

In this exercise, the shapes (circle, rectangle, triangle) share common methods (area, perimeter, and describe), but each implements these actions uniquely according to their properties.

## 📝 Instructions

1. Create the base class `Shape`. The **Shape** class will act as a template for other shapes. It will contain methods that will be overridden by specific shapes.

2. Include the methods:
   - **area:** Returns 0 by default.
   - **perimeter:** Returns 0 by default.
   - **describe:** Returns a generic message like: `Generic shape`

3. Create the derived class `Circle`. This class needs an attribute `radius`.
4. Create the derived class `Rectangle`. This class needs the attributes `width` and `height`.
5. Create the derived class `Triangle`. This class needs the attributes `side1`, `side2`, `side3`, `height`.
6. **Overridden methods.** Override the methods `area, perimeter, and describe` and implement the specific formulas to calculate area and perimeter, and adjust the describe method for each shape.
7. Create instances of each shape and verify that the methods work correctly. For example:

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
