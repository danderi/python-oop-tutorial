import pytest


@pytest.mark.it("Should check if Student class is declared")
def test_class_declaration():
    import app
    # Verificamos si la clase Person existe en el módulo app
    assert hasattr(app, "Student"), "The Student class is not declared in app.py"



@pytest.mark.it("Should have the correct school_name attribute")
def test_school_name():
    from app import Student 
    # Verifica que el atributo de clase school_name sea 'Python Academy'
    assert Student.school_name == "Python Academy", "El atributo de clase school_name no es el esperado"


@pytest.mark.it("Should initialize attributes correctly: name, age, grade")
def test_student_attributes():
    from app import Student 
    # Verifica que el constructor inicializa correctamente los atributos
    student = Student("Alice", 15, "10th")
    assert student.name == "Alice", "El nombre del estudiante no se inicializó correctamente"
    assert student.age == 15, "La edad del estudiante no se inicializó correctamente"
    assert student.grade == "10th", "El grado del estudiante no se inicializó correctamente"


@pytest.mark.it("Should return the correct student_info string")
def test_student_info():
    from app import Student 
    # Verifica que el método student_info devuelva la salida esperada
    student = Student("Alice", 15, "10th")
    expected_info = "Alice is 15 years old in 10th grade at Python Academy"
    assert student.student_info() == expected_info, f"La salida del método student_info es incorrecta. Esperado: {expected_info}"
