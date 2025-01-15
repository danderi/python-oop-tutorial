# DataManager that uses any processor
class DataManager:
    """Class that works with any data processor through duck typing"""
    def __init__(self, processor):
        """Initialize with any processor that supports the required methods"""
        self.processor = processor

    def process_data(self, data):
        self.processor.load_data(data)
        self.processor.process()
        return self.processor.export()
    

# Processor for JSON
class JsonProcessor:
    def load_data(self, data):
        self.data = f"Loading JSON data: {data}"

    def process(self):
        self.data = f"Processing JSON data: {self.data.upper()}"

    def export(self):
        return f"Exporting JSON data: {self.data}"

# Processor for CSV
class CsvProcessor:
    def load_data(self, data):
        self.data = f"Loading CSV data: {data}"

    def process(self):
        self.data = f"Processing CSV data: {self.data.upper()}"

    def export(self):
        return f"Exporting CSV data: {self.data}"

# Processor for XML
class XmlProcessor:
    def load_data(self, data):
        self.data = f"Loading XML data: {data}"

    def process(self):
        self.data = f"Processing XML data: {self.data.upper()}"

    def export(self):
        return f"Exporting XML data: {self.data}"

    


# Test code
if __name__ == "__main__":
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
