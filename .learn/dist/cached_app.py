class DataManager:
    """Class that works with any data processor through duck typing"""
    def __init__(self, processor):
        self.processor = processor
    
    def process_data(self, data):
        self.processor.load_data(data)
        self.processor.process()
        return self.processor.export()


class JsonProcessor:
    def load_data(self, data):
        self.data = f"Loading JSON data: {data}"

    def process(self):
        self.data = self.data.upper()

    def export(self):
        return f"Exporting JSON data: {self.data}"


class CsvProcessor:
    def load_data(self, data):
        self.data = f"Loading CSV data: {data}"

    def process(self):
        self.data = self.data.lower()

    def export(self):
        return f"Exporting CSV data: {self.data}"


class XmlProcessor:
    def load_data(self, data):
        self.data = f"Loading XML data: {data}"

    def process(self):
        self.data = self.data[::-1]

    def export(self):
        return f"Exporting XML data: {self.data}"
    

json_data = '{"name": "John", "age": 30}'
csv_data = 'name,age\nJohn,30'
xml_data = '<person><name>John</name><age>30</age></person>'

json_proc = JsonProcessor()
csv_proc = CsvProcessor()
xml_proc = XmlProcessor()