# Making Smart Data Handlers - The Duck Typing Way! 🦆

Hey there! Let's learn about something fun called "duck typing" by building different ways to handle data. You know how they say "if it walks like a duck and quacks like a duck, it's a duck"? That's exactly what we're going to do with code!

## Why Are We Making This? 📊

Think about different file types on your computer:
- Some files are JSON (like settings files)
- Some are CSV (like spreadsheets)
- Some are XML (like web data)
- They're different, but we want to handle them all easily!

This is perfect for learning duck typing because:
- Each format needs to be handled differently
- But we want to use them all in the same way
- We don't care what type they are, just what they can do!

## What We'll Build 🛠️

1. We'll create three different data handlers:
   - `JsonProcessor` for JSON data (like web settings)
   - `CsvProcessor` for CSV data (like spreadsheet files)
   - `XmlProcessor` for XML data (like web pages)

2. Each processor will know how to:
   - Load data from a string
   - Process the data (make it uppercase in our example)
   - Export the processed data

3. Then we'll make a smart `DataManager` that:
   - Doesn't care which processor it gets
   - Just uses whatever processor you give it
   - Works with any processor that has the right methods

## 💡 Need Help?

- No need for inheritance or abstract classes
- Just make sure each processor has the same method names
- Focus on what things can do, not what they are
- Think "if it can process data, it's a processor!"

## Why Duck Typing? 🦆

Duck typing is cool because:
1. It's super flexible - add new processors anytime!
2. No complicated relationships between classes
3. Just make sure things can do what's needed
4. Like having different remote controls that all have a power button

## What Should Happen? 🎯

When you run your code:
```python
# Create your processors
json_proc = JsonProcessor()
csv_proc = CsvProcessor()
xml_proc = XmlProcessor()

# Test with different data
json_data = '{"name": "John", "age": 30}'
csv_data = 'name,age\nJohn,30'
xml_data = '<person><name>John</name><age>30</age></person>'

# Process each type
for processor, data in [(json_proc, json_data), 
                       (csv_proc, csv_data),
                       (xml_proc, xml_data)]:
    manager = DataManager(processor)
    manager.process_data(data)
    print(manager.get_processed_data())  # Each processor shows its results!

# Make a custom processor - it just works!
class CustomProcessor:
    def load_data(self, data): pass
    def process(self): pass
    def export(self): return "Custom processed data"

custom = DataManager(CustomProcessor())  # Works just fine!
```

Think of it like having different kitchen tools - as long as they can chop vegetables, it doesn't matter if it's a knife, food processor, or fancy gadget. If it can do the job, it works! 🔨