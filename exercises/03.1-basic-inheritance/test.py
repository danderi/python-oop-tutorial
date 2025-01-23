import pytest
from unittest.mock import patch
from io import StringIO
import importlib

@pytest.mark.it("Should define a class called 'Animal'")
def test_animal_class_defined():
    import app
   
    assert hasattr(app, "Animal"), "The class 'Animal' should be defined"

@pytest.mark.it("Should initialize 'Animal' with attributes 'name' and 'species'")
def test_animal_init():
    import app
    animal = app.Animal("Generic Animal", "Unknown")
    assert animal.name == "Generic Animal", "The 'name' attribute is not correctly initialized"
    assert animal.species == "Unknown", "The 'species' attribute is not correctly initialized"

@pytest.mark.it("Should have a method 'make_sound' in 'Animal' that prints 'Some generic sound'")
def test_animal_make_sound():
    import app
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        animal = app.Animal("Generic Animal", "Unknown")
        animal.make_sound()
        output = mock_stdout.getvalue().strip()
    assert output == "Some generic sound", f"Expected 'Some generic sound', but got '{output}'"

@pytest.mark.it("Should define a class called 'Dog' that inherits from 'Animal'")
def test_dog_class_defined():
    import app
    assert hasattr(app, "Dog"), "The class 'Dog' should be defined"
    assert issubclass(app.Dog, app.Animal), "The class 'Dog' should inherit from 'Animal'"

@pytest.mark.it("Should initialize 'Dog' with 'name' and 'species', calling the parent constructor")
def test_dog_init():
    import app
    dog = app.Dog("Buddy", "Canine")
    assert dog.name == "Buddy", "The 'name' attribute of 'Dog' is not correctly initialized"
    assert dog.species == "Canine", "The 'species' attribute of 'Dog' is not correctly initialized"

@pytest.mark.it("Should override 'make_sound' in 'Dog' to print 'Woof!'")
def test_dog_make_sound():
    import app
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        dog = app.Dog("Buddy", "Canine")
        dog.make_sound()
        output = mock_stdout.getvalue().strip()
    assert output == "Woof!", f"Expected 'Woof!', but got '{output}'"

@pytest.mark.it("Should add a method 'fetch' to 'Dog' that prints '<name> is fetching the ball'")
def test_dog_fetch():
    import app
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        dog = app.Dog("Buddy", "Canine")
        dog.fetch()
        output = mock_stdout.getvalue().strip()
    assert output == "Buddy is fetching the ball", f"Expected 'Buddy is fetching the ball', but got '{output}'"

@pytest.mark.it("Should print the expected output when creating a Dog and calling make_sound and fetch")
def test_app_full_output():
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        import app  # Import the file that contains your main code
        importlib.reload(app)  # Reload the module to ensure it runs from the start
        
        # Expected output after running app.py
        expected = "Woof!\nBuddy is fetching the ball"
        
        # Capture the actual output
        output = mock_stdout.getvalue().strip()
        
    # Assert the output matches the expected
    assert output == expected, f"Expected output to be:\n{expected}\nBut got:\n{output}"
