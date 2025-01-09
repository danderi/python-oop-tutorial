class Temperature:
    def __init__(self, celsius):
        self.__celsius = None  # Initialize to None first
        self.celsius = celsius  # Use the setter for validation
    
    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below -273.15°C")
        self.__celsius = float(value)
    
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

# Test code
if __name__ == "__main__":
    temp = Temperature(25)
    print(temp.celsius)     # 25.0
    print(temp.fahrenheit)  # 77.0
    
    temp.celsius = 30
    print(temp.celsius)     # 30.0
    print(temp.fahrenheit)  # 86.0
    
    try:
        temp.celsius = -300
    except ValueError as e:
        print(str(e))      # "Temperature cannot be below -273.15°C"
