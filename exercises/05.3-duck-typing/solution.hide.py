import json
import csv
import xml.etree.ElementTree as ET
from io import StringIO

class JsonProcessor:
    def __init__(self):
        self.data = None
        self.processed_data = None
    
    def load_data(self, data_string):
        """Load JSON data from string"""
        self.data = json.loads(data_string)
    
    def process(self):
        """Process JSON data"""
        if self.data:
            self.processed_data = {k: str(v).upper() for k, v in self.data.items()}
    
    def export(self):
        """Export processed data as JSON string"""
        return json.dumps(self.processed_data) if self.processed_data else "{}"

class CsvProcessor:
    def __init__(self):
        self.data = None
        self.processed_data = None
    
    def load_data(self, data_string):
        """Load CSV data from string"""
        reader = csv.DictReader(StringIO(data_string))
        self.data = next(reader)  # Get first row
    
    def process(self):
        """Process CSV data"""
        if self.data:
            self.processed_data = {k: v.upper() for k, v in self.data.items()}
    
    def export(self):
        """Export processed data as CSV string"""
        if not self.processed_data:
            return ""
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=self.processed_data.keys())
        writer.writeheader()
        writer.writerow(self.processed_data)
        return output.getvalue().strip()

class XmlProcessor:
    def __init__(self):
        self.data = None
        self.processed_data = None
    
    def load_data(self, data_string):
        """Load XML data from string"""
        root = ET.fromstring(data_string)
        self.data = {child.tag: child.text for child in root}
    
    def process(self):
        """Process XML data"""
        if self.data:
            self.processed_data = {k: v.upper() for k, v in self.data.items()}
    
    def export(self):
        """Export processed data as XML string"""
        if not self.processed_data:
            return "<data></data>"
        root = ET.Element("data")
        for key, value in self.processed_data.items():
            child = ET.SubElement(root, key)
            child.text = value
        return ET.tostring(root, encoding='unicode')

class DataManager:
    """Class that works with any data processor through duck typing"""
    def __init__(self, processor):
        """Initialize with any processor that supports the required methods"""
        self.processor = processor
    
    def process_data(self, data):
        """Process data using the provided processor"""
        self.processor.load_data(data)
        self.processor.process()
    
    def get_processed_data(self):
        """Get the processed data in the processor's format"""
        return self.processor.export()

# Test code
if __name__ == "__main__":
    # Create processors
    json_proc = JsonProcessor()
    csv_proc = CsvProcessor()
    xml_proc = XmlProcessor()
    
    # Sample data
    json_data = '{"name": "John", "age": "30"}'
    csv_data = 'name,age\nJohn,30'
    xml_data = '<person><name>John</name><age>30</age></person>'
    
    # Process each type
    for processor, data in [(json_proc, json_data), 
                           (csv_proc, csv_data),
                           (xml_proc, xml_data)]:
        manager = DataManager(processor)
        manager.process_data(data)
        print(f"\nProcessed data from {processor.__class__.__name__}:")
        print(manager.get_processed_data())
    
    # Test with a custom processor
    class CustomProcessor:
        def load_data(self, data): pass
        def process(self): pass
        def export(self): return "Custom processed data"
    
    custom = DataManager(CustomProcessor())
    custom.process_data("any data")
    print("\nCustom processor result:")
    print(custom.get_processed_data())
