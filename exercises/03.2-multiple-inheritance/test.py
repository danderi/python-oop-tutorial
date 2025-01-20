import pytest
from unittest.mock import patch
from io import StringIO
import importlib

@pytest.mark.it("Should define the 'Flying' class with a 'fly' method that prints '¡Puedo volar!'")
def test_flying_class():
    import app
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        flying_instance = app.Flying()
        flying_instance.fly()
        output = mock_stdout.getvalue().strip()
    assert output == "I can fly!", f"Expected '¡Puedo volar!', but got '{output}'"

@pytest.mark.it("Should define the 'Swimming' class with a 'swim' method that prints '¡Puedo nadar!'")
def test_swimming_class():
    import app
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        swimming_instance = app.Swimming()
        swimming_instance.swim()
        output = mock_stdout.getvalue().strip()
    assert output == "I can swim!", f"Expected '¡Puedo nadar!', but got '{output}'"

@pytest.mark.it("Should define the 'Bird' class with attributes 'name' and 'species'")
def test_bird_class_init():
    import app
    bird = app.Bird("Generic Bird", "Unknown")
    assert bird.name == "Generic Bird", "The 'name' attribute is not correctly initialized"
    assert bird.species == "Unknown", "The 'species' attribute is not correctly initialized"

@pytest.mark.it("Should define the 'Duck' class that inherits from Bird, Flying, and Swimming")
def test_duck_class_inheritance():
    import app
    duck = app.Duck("Donald", "Mallard")
    assert isinstance(duck, app.Duck), "The object is not an instance of Duck"
    assert isinstance(duck, app.Bird), "Duck should inherit from Bird"
    assert isinstance(duck, app.Flying), "Duck should inherit from Flying"
    assert isinstance(duck, app.Swimming), "Duck should inherit from Swimming"

@pytest.mark.it("Should print the correct introduction for Duck")
def test_duck_introduction():
    import app
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        duck = app.Duck("Donald", "Mallard")
        duck.introduce()
        output = mock_stdout.getvalue().strip()
    assert output == "I'm Donald, a Mallard that can both fly and swim!", f"Expected '¡Soy Donald, un Mallard que puede volar y nadar!', but got '{output}'"

@pytest.mark.it("Should print 'I can fly!' when calling fly() on Duck")
def test_duck_fly():
    import app
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        duck = app.Duck("Donald", "Mallard")
        duck.fly()
        output = mock_stdout.getvalue().strip()
    assert output == "I can fly!", f"Expected 'I can fly!', but got '{output}'"

@pytest.mark.it("Should print 'I can swim!' when calling swim() on Duck")
def test_duck_swim():
    import app
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        duck = app.Duck("Donald", "Mallard")
        duck.swim()
        output = mock_stdout.getvalue().strip()
    assert output == "I can swim!", f"Expected 'I can swim!', but got '{output}'"

