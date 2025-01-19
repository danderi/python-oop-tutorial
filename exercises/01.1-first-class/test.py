import pytest
from io import StringIO
from unittest.mock import patch


@pytest.mark.it("Should check if Person class is declared")
def test_class_declaration():
    import app
    # Verificamos si la clase Person existe en el módulo app
    assert hasattr(app, "Person"), "The Person class is not declared in app.py"


# Test 1: Verificar que el atributo name se asigna correctamente
@pytest.mark.it("Should correctly assign the name attribute")
def test_person_initialization():
    from app import Person
    person = Person("John")
    assert person.name == "John", "The name attribute was not set correctly"


@pytest.mark.it("Should check if greet method is declared in Person class")
def test_method_declared():
    from app import Person
    # Verificamos si el método greet está presente en la clase Person
    person = Person("John")
    assert hasattr(person, "greet"), "The greet method is not declared in the Person class"




