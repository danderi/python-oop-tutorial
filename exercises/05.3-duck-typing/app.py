class DataManager:
    """Class that works with any data processor through duck typing"""
    def __init__(self, processor):
        """Initialize with any processor that supports the required methods"""
        self.processor = processor
    
    def process_data(self, data):
        """Process data using the provided processor"""
        # write your code here
        pass

# Create your JsonProcessor class here

# Create your CsvProcessor class here

# Create your XmlProcessor class here
