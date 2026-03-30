# Create your Temperature class here with properties for celsius and fahrenheit
class Temperature:
    def __init__(self, celsius):
        self.__celsius = None
        self.celsius = celsius  # usamos el setter para validar desde el inicio

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:
            self.__celsius = value
        else:
            print("Temperature too low. Cannot be set.")

    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        celsius_value = (value - 32) * 5/9
        self.celsius = celsius_value  # reutilizamos validación  