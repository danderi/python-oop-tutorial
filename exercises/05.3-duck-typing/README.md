# Creating Smart Data Handlers - Duck Typing Style! 🦆

Let's learn something fun called "duck typing" by building different ways to handle data. You know how they say "if it walks like a duck and quacks like a duck, it's a duck"? That's exactly what we're going to do with code!

For this exercise, we will create different data processors **(JsonProcessor, CsvProcessor, XmlProcessor)** and a generic **DataManager** that can work with any of them, without worrying about what type they are. This is useful for learning duck typing because each format needs to be handled differently, plus:

- We focus on behavior, not inheritance or class types.
- We can add new processors without changing existing code.
- It's a perfect example of Python's flexibility.

Let's get started!

## Instructions

1. Define 3 classes to handle data in different formats `JsonProcessor, CsvProcessor, XmlProcessor` and define the following methods for each processor: `load_data(data), process(), export()`

```python
# Example
class JsonProcessor:
   def load_data(self, data):
      self.data = f"Loading JSON data: {data}"

   def process(self):
      self.data = self.data.upper()  # Convert to uppercase as an example

   def export(self):
      return f"Exporting JSON data: {self.data}"
```

2. Then define a `DataManager` class that has a `process_data(data)` method and works with any processor that has the methods:

- load_data: to load data.
- process: to process it.
- export: to export it.

The DataManager should not care which processor it receives, just use any processor you give it.

3. **Test your solution.** Create instances of the `JsonProcessor, CsvProcessor, XmlProcessor` classes and verify that they work correctly.

```python
# Create your processors
json_proc = JsonProcessor()
csv_proc = CsvProcessor()
xml_proc = XmlProcessor()

# Test with different data
json_data = '{"name": "John", "age": 30}'
csv_data = 'name,age\nJohn,30'
xml_data = '<person><name>John</name><age>30</age></person>'

# JSON Processor
manager = DataManager(json_proc)
print(manager.process_data(json_data))  # Process and display results for JSON

# CSV Processor
manager = DataManager(csv_proc)
print(manager.process_data(csv_data))  # Process and display results for CSV

# XML Processor
manager = DataManager(xml_proc)
print(manager.process_data(xml_data))  # Process and display results for XML
```

## 💡 Tips

- You don't need inheritance or abstract classes
- Just make sure each processor has the same method names
- Focus on what things can do, not what they are
- Think "if it can process data, it's a processor!"
