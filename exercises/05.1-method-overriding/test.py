import math
import pytest
from app import Shape

@pytest.mark.it("Should verify the base class 'Shape' has default methods working correctly")
def test_forma_base():
    forma = Shape()
    assert forma.area() == 0, "The `area` method of `Shape` should return 0 by default"
    assert forma.perimeter() == 0, "The `perimeter` method of `Shape` should return 0 by default"
    assert forma.describe().lower() == "generic shape", "The `describe` method of `Shape` should return 'Generic shape' by default"


@pytest.mark.it("Should declare 'Circle', 'Rectangle', and 'Triangle' classes")
def test_names_array_declaration():
    import app  # Import the app module
    import importlib
    importlib.reload(app)  # Reload the module to ensure it reflects recent changes
    
    assert hasattr(app, 'Circle'), "'Circle' class is not declared in app.py"
    assert hasattr(app, 'Rectangle'), "'Rectangle' class is not declared in app.py"
    assert hasattr(app, 'Triangle'), "'Triangle' class is not declared in app.py"
    
@pytest.mark.it("Create the 'Circle' class with a radius attribute and methods to calculate area, perimeter, and description")
def test_circle_properties_creation():
    from app import Circle

    circle = Circle(5)
    assert circle.radius == 5, "The radius attribute was not set correctly."

@pytest.mark.it("Create the 'Rectangle' class with width and height attributes and methods to calculate area, perimeter, and description")
def test_rectangle_properties_creation():
    from app import Rectangle

    rectangle = Rectangle(4, 6)
    assert rectangle.width == 4, "The width attribute was not set correctly."
    assert rectangle.height == 6, "The height attribute was not set correctly."

@pytest.mark.it("Create the 'Triangle' class with side1, side2, side3, and height attributes and methods to calculate area, perimeter, and description")
def test_triangle_properties_creation():
    from app import Triangle

    triangle = Triangle(3, 4, 5, 4)
    assert triangle.side1 == 3, "The side1 attribute was not set correctly."
    assert triangle.side2 == 4, "The side2 attribute was not set correctly."
    assert triangle.side3 == 5, "The side3 attribute was not set correctly."
    assert triangle.height == 4, "The height attribute was not set correctly."

@pytest.mark.it("Should verify the `Circle` class calculates area, perimeter, and description correctly")
def test_circle():
    from app import Circle

    circle = Circle(5)
    assert math.isclose(circle.area(), math.pi * 5**2, rel_tol=1e-2), "The `area` method of `Circle` should calculate πr²"
    assert math.isclose(circle.perimeter(), 2 * math.pi * 5, rel_tol=1e-2), "The `perimeter` method of `Circle` should calculate 2πr"
    assert circle.describe().lower() == f"circle with radius 5 - area: {circle.area()}, perimeter: {circle.perimeter()}", "The `describe` method of `Circle` should return the correct description"

@pytest.mark.it("Should verify the `Rectangle` class calculates area, perimeter, and description correctly")
def test_rectangle():
    from app import Rectangle

    rectangle = Rectangle(4, 6)
    assert rectangle.area() == 24, "The `area` method of `Rectangle` should calculate width * height"
    assert rectangle.perimeter() == 20, "The `perimeter` method of `Rectangle` should calculate 2 * (width + height)"
    assert rectangle.describe().lower() == f"rectangle 4x6 - area: {rectangle.area()}, perimeter: {rectangle.perimeter()}", "The `describe` method of `Rectangle` should return the correct description"

@pytest.mark.it("Should verify the `Triangle` class calculates area, perimeter, and description correctly")
def test_triangle():
    from app import Triangle

    triangle = Triangle(3, 4, 5, 4)
    assert triangle.area() == 6, "The `area` method of `Triangle` should calculate (base * height) / 2"
    assert triangle.perimeter() == 12, "The `perimeter` method of `Triangle` should calculate side1 + side2 + side3"
    assert triangle.describe().lower() == f"triangle with sides 3,4,5 - area: {triangle.area()}, perimeter: {triangle.perimeter()}", "The `describe` method of `Triangle` should return the correct description"
