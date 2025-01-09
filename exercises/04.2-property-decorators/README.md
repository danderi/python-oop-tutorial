# Property Decorators and Getters/Setters

## 📝 Instructions

1. Create a class called `Temperature` in `app.py` that:
   - Uses a private attribute `__celsius` to store temperature
   - Implements `@property` decorator for both Celsius and Fahrenheit readings
   - Includes proper setters with validation

2. Requirements:
   - Temperature in Celsius cannot be set below absolute zero (-273.15°C)
   - Both Celsius and Fahrenheit properties should be accessible
   - Use appropriate property decorators (`@property`, `@celsius.setter`)
   - Include validation in setters to ensure valid temperatures

## 💡 Hints

- Use `@property` to create read-only attributes
- Use `@name.setter` to create setter methods
- Remember to validate temperatures in setters
- The formula for Fahrenheit is: (C × 9/5) + 32

## Expected Output
```python
temp = Temperature(25)
print(temp.celsius)     # Should print: 25.0
print(temp.fahrenheit)  # Should print: 77.0

temp.celsius = 30
print(temp.celsius)     # Should print: 30.0
print(temp.fahrenheit)  # Should print: 86.0

# This should raise a ValueError
try:
    temp.celsius = -300
except ValueError as e:
    print(str(e))      # Should print: "Temperature cannot be below -273.15°C"
```

## Why Properties?

Properties provide several advantages over direct attribute access:
1. **Data Validation**: Control and validate values before assignment
2. **Computed Attributes**: Calculate values on-the-fly (like Fahrenheit conversion)
3. **Encapsulation**: Change internal implementation without affecting external code
4. **Read-Only Attributes**: Prevent unauthorized modifications
