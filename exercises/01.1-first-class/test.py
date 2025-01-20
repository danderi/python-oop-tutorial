import pytest
from io import StringIO
from unittest.mock import patch
import importlib


@pytest.mark.it("Should check if Person class is declared")
def test_class_declaration():
    import app

    assert hasattr(app, "Person"), "The Person class is not declared in app.py"



@pytest.mark.it("Should correctly assign the name attribute")
def test_person_initialization():
    from app import Person
    person = Person("John")
    assert person.name == "John", "The name attribute was not set correctly"


@pytest.mark.it("Should check if greet method is declared in Person class")
def test_method_declared():
    from app import Person
   
    person = Person("John")
    assert hasattr(person, "greet"), "The greet method is not declared in the Person class"



@pytest.mark.it("Should print the results of Person in app.py")
def test_app_prints_greetings():
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        import app  # Import the file that contains your main code
        importlib.reload(app)  # Reimport the module to ensure the code runs
        output = mock_stdout.getvalue().strip()

  
    expected = "Hello, my name is John"

    assert output == expected, f"Expected output to be '{expected}', but got '{output}'"