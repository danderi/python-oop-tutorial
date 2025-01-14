import unittest
from app import DataManager, JsonProcessor, CsvProcessor, XmlProcessor

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.json_proc = JsonProcessor()
        self.csv_proc = CsvProcessor()
        self.xml_proc = XmlProcessor()

    def test_json_processor_methods(self):
        self.assertTrue(hasattr(self.json_proc, 'load_data'))
        self.assertTrue(hasattr(self.json_proc, 'process'))
        self.assertTrue(hasattr(self.json_proc, 'export'))
        self.json_proc.load_data('{"name": "John", "age": 30}')
        self.json_proc.process()
        self.json_proc.export()

    def test_csv_processor_methods(self):
        self.assertTrue(hasattr(self.csv_proc, 'load_data'))
        self.assertTrue(hasattr(self.csv_proc, 'process'))
        self.assertTrue(hasattr(self.csv_proc, 'export'))
        self.csv_proc.load_data('name,age\nJohn,30')
        self.csv_proc.process()
        self.csv_proc.export()

    def test_xml_processor_methods(self):
        self.assertTrue(hasattr(self.xml_proc, 'load_data'))
        self.assertTrue(hasattr(self.xml_proc, 'process'))
        self.assertTrue(hasattr(self.xml_proc, 'export'))
        self.xml_proc.load_data('<person><name>John</name><age>30</age></person>')
        self.xml_proc.process()
        self.xml_proc.export()

    def test_data_manager_with_json(self):
        manager = DataManager(self.json_proc)
        manager.process_data('{"name": "John", "age": 30}')

    def test_data_manager_with_csv(self):
        manager = DataManager(self.csv_proc)
        manager.process_data('name,age\nJohn,30')

    def test_data_manager_with_xml(self):
        manager = DataManager(self.xml_proc)
        manager.process_data('<person><name>John</name><age>30</age></person>')

if __name__ == "__main__":
    unittest.main()