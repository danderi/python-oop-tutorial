# Duck Typing and Protocol Implementation

## 📝 Instructions

1. Create three data processor classes in `app.py`:
   - `JsonProcessor` that handles JSON data
   - `CsvProcessor` that handles CSV data
   - `XmlProcessor` that handles XML data

2. Each processor should implement these methods:
   - `load_data(data_string)` - Loads data from a string
   - `process()` - Processes the loaded data
   - `export()` - Returns processed data in a specific format

3. Create a `DataManager` class that:
   - Takes any processor as input
   - Doesn't care about the processor's type
   - Only requires that the processor implements the necessary methods

## 💡 Hints

- No inheritance or abstract classes needed
- Classes only need to share method names
- Focus on behavior rather than type
- Use proper error handling for invalid data

## Why Duck Typing?

Duck typing in Python means:
1. Objects are defined by behavior, not class
2. No formal interface definitions needed
3. More flexible than classical inheritance
4. "If it walks like a duck and quacks like a duck, it's a duck"

## Expected Output
```python
# Create processors
json_proc = JsonProcessor()
csv_proc = CsvProcessor()
xml_proc = XmlProcessor()

# Sample data
json_data = '{"name": "John", "age": 30}'
csv_data = 'name,age\nJohn,30'
xml_data = '<person><name>John</name><age>30</age></person>'

# Process each type
for processor, data in [(json_proc, json_data), 
                       (csv_proc, csv_data),
                       (xml_proc, xml_data)]:
    manager = DataManager(processor)
    manager.process_data(data)
    print(manager.get_processed_data())  # Should show processed data in each format

# This should work with any processor that implements the required methods
class CustomProcessor:
    def load_data(self, data): pass
    def process(self): pass
    def export(self): return "Custom processed data"

custom = DataManager(CustomProcessor())  # Should work fine
```
