import pytest
import importlib
from unittest.mock import patch
from io import StringIO


@pytest.mark.it("Should check if Student class is declared")
def test_class_declaration():
    import app
   
    assert hasattr(app, "Student"), "The Student class is not declared in app.py"



@pytest.mark.it("Should have the correct school_name attribute")
def test_school_name():
    from app import Student 
   
    assert Student.school_name == "Python Academy", "El atributo de clase school_name no es el esperado"


@pytest.mark.it("Should initialize attributes correctly: name, age, grade")
def test_student_attributes():
    from app import Student 
  
    student = Student("Alice", 15, "10th")
    assert student.name == "Alice", "El nombre del estudiante no se inicializó correctamente"
    assert student.age == 15, "La edad del estudiante no se inicializó correctamente"
    assert student.grade == "10th", "El grado del estudiante no se inicializó correctamente"


@pytest.mark.it("Should return the correct student_info string")
def test_student_info():
    from app import Student 
  
    student = Student("Alice", 15, "10th")
    expected_info = "Alice is 15 years old in 10th grade at Python Academy"
    assert student.student_info() == expected_info, f"La salida del método student_info es incorrecta. Esperado: {expected_info}"

@pytest.mark.it("Should print the results of student_info() in Student")
def test_app_prints_student_info():
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        import app  # Import the file that contains your main code
        importlib.reload(app)  # Reimport the module to ensure the code runs
        output = [line.strip() for line in mock_stdout.getvalue().strip().split("\n")]

    # Define the expected values in the correct order
    expected = [
        "Alice is 15 years old in 10th grade at Python Academy",
        "Bob is 16 years old in 11th grade at Python Academy"
    ]

    # Assert to check the output matches the expected values
    assert output == expected, f"Expected output to be '{expected}', but got '{output}'"