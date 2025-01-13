# Creating a Smart Temperature Converter! 🌡️

Let's create something cool: a temperature converter smart enough to prevent impossible temperatures. We'll use something called "properties" to make this work smoothly.

In most countries, we use Celsius, but sometimes we need Fahrenheit (like when reading weather reports from the United States). We can't have temperatures below absolute zero (-273.15°C), so we want to convert between them easily and safely.

This exercise is perfect for learning about properties, as we need to verify that temperatures are possible before using them. We want to easily switch between Celsius and Fahrenheit, and protect our temperature data from errors.

## 📝 Instructions

1. **Create the `Temperature` class**. The class should have a private attribute to store the temperature in degrees Celsius.

2. **Using properties**. Create the property for Celsius within the `Temperature` class to read and set the temperature in Celsius safely. To do this, we use the **@property** decorator. This turns the method into a "getter", allowing the value to be accessed as if it were an attribute, without needing to call the method directly.

```python
    @property
    def celsius(self):
        return self.__celsius
```

3. **Create the setter for Celsius.** We want to ensure that the value we set for Celsius is valid (greater than or equal to -273.15°C), so we use the **@celsius.setter** decorator to control how the Celsius value is set.

```python
    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:
            self.__celsius = value
        else:
            print("Temperature too low. Cannot be set.")
```

4. **Create the property for Fahrenheit.** To convert between Celsius and Fahrenheit, we need a property for Fahrenheit. This is a **"getter"** that converts the temperature from Celsius to Fahrenheit.

```python
    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32
```

5. **Create the setter for Fahrenheit.** We also need a **"setter"** for Fahrenheit, so we can set the temperature in degrees Fahrenheit and then automatically convert it to degrees Celsius. Remember that the formula to convert from Fahrenheit to Celsius is: C = (F - 32) * 5/9.

6. **Test your solution.** Create an instance of the `Temperature` class called `temp` with:

```python
temp: 25
```
-

- Print the temperature in Celsius
- Print the temperature in Fahrenheit
- Use the **fahrenheit setter** to change the temperature to 100°F. Then, print the temperature in Celsius to verify that the conversion was done correctly.

```python
temp.fahrenheit = 100
```
-

- Set an impossible temperature (below absolute zero), for example, -300°C. This should trigger an error message indicating that the temperature cannot be set.

By following these steps, you should see something similar to the following:

```python
25
77
37.77777777777778
Temperature too low. Cannot be set.
```

## Why use properties? 🎓

Properties are very useful because:
1. They check if values make sense before using them
2. They automatically calculate things when necessary
3. They make it easy to change how things work without breaking other code
4. They keep our data safe from accidents

Think of properties as having a smart thermostat: it won't let you set impossible temperatures and can show you the temperature in the format you want. 🌟
