import pytest
from io import StringIO
from unittest.mock import patch
from app import Temperature

@pytest.mark.it("Should verify that the properties 'celsius' and 'fahrenheit' are defined")
def test_temperature_properties_exist():
    temp = Temperature(0)  
    assert isinstance(Temperature.celsius, property), "The 'celsius' property is not defined."
    assert isinstance(Temperature.fahrenheit, property), "The 'fahrenheit' property is not defined."

@pytest.mark.it("Should verify the functionality of the 'celsius' and 'fahrenheit' setters")
def test_temperature_setters():
    temp = Temperature(0)  
    
    temp.celsius = 100
    assert temp.celsius == 100, f"Expected Celsius value 100, but got {temp.celsius}"
    assert temp.fahrenheit == 212, f"Expected Fahrenheit value 212, but got {temp.fahrenheit}"

    temp.fahrenheit = 32
    assert temp.celsius == 0, f"Expected Celsius value 0, but got {temp.celsius}"
    assert temp.fahrenheit == 32, f"Expected Fahrenheit value 32, but got {temp.fahrenheit}"


@pytest.mark.it("Should correctly convert between Celsius and Fahrenheit")
def test_temperature_conversion():
    temp = Temperature(25)
    
    assert temp.celsius == 25, f"Expected Celsius value 25, but got {temp.celsius}"
    assert temp.fahrenheit == 77, f"Expected Fahrenheit value 77, but got {temp.fahrenheit}"

    temp.fahrenheit = 100
    assert temp.celsius == 37.77777777777778, f"Expected Celsius value 37.77777777777778, but got {temp.celsius}"

@pytest.mark.it("Should handle setting impossible temperatures")
def test_impossible_temperature():
    temp = Temperature(25)
    
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        temp.celsius = -300  
        output = mock_stdout.getvalue().strip()
        expected_output = "Temperature too low. Cannot be set.".lower()
        assert output.lower() == expected_output, f"Expected error message '{expected_output}', but got '{output}'"
