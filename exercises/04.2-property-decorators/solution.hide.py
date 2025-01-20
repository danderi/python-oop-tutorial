class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:
            self._celsius = value
        else:
            print("Temperature too low. Cannot be set.")
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

# Test code
if __name__ == "__main__":
    temp = Temperature(25)
    print(temp.celsius)     # 25.0
    print(temp.fahrenheit)  # 77.0
    temp.celsius = 100
    print(temp.celsius)     # 37.777
    temp.celsius = -300 # "Temperature too low. Cannot be set."
