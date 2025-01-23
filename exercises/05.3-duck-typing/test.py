import pytest


@pytest.mark.it("Should define the JsonProcessor class with the methods load_data, process, and export")
def test_json_processor():
    from app import JsonProcessor

    json_proc = JsonProcessor()
    assert hasattr(json_proc, 'load_data'), "JsonProcessor should have a load_data method"
    assert hasattr(json_proc, 'process'), "JsonProcessor should have a process method"
    assert hasattr(json_proc, 'export'), "JsonProcessor should have an export method"

@pytest.mark.it("Should define the CsvProcessor class with the methods load_data, process, and export")
def test_csv_processor():
    from app import CsvProcessor

    csv_proc = CsvProcessor()
    assert hasattr(csv_proc, 'load_data'), "CsvProcessor should have a load_data method"
    assert hasattr(csv_proc, 'process'), "CsvProcessor should have a process method"
    assert hasattr(csv_proc, 'export'), "CsvProcessor should have an export method"

@pytest.mark.it("Should define the XmlProcessor class with the methods load_data, process, and export")
def test_xml_processor():
    from app import XmlProcessor

    xml_proc = XmlProcessor()
    assert hasattr(xml_proc, 'load_data'), "XmlProcessor should have a load_data method"
    assert hasattr(xml_proc, 'process'), "XmlProcessor should have a process method"
    assert hasattr(xml_proc, 'export'), "XmlProcessor should have an export method"



@pytest.mark.it("Should call the load_data, process, and export methods on the 'processe_data' method")
def test_process_data_calls_methods():
    from app import DataManager
    from unittest.mock import MagicMock
    processor = MagicMock()
    manager = DataManager(processor)

    data = "some data"
    manager.process_data(data)

    processor.load_data.assert_called_once_with(data)
    processor.process.assert_called_once()
    processor.export.assert_called_once()


@pytest.mark.it("Should declare the variables json_data, csv_data, and xml_data for make testing")
def test_variables_declared_for_testing():
        import app  
        assert hasattr(app, 'json_data'), "The variable 'json_data' is not defined in app.py."
        assert hasattr(app, 'csv_data'), "The variable 'csv_data' is not defined in app.py."
        assert hasattr(app, 'xml_data'), "The variable 'xml_data' is not defined in app.py."


@pytest.mark.it("Should declare the object json_proc, csv_proc, and xml_proc instances of JsonProcessor, CsvProcessor, and XmlProcessor respectively")
def test_objects_instances():
        import app  
        assert hasattr(app, 'json_proc'), "The object 'json_proc' is not defined in app.py."
        assert hasattr(app, 'csv_proc'), "The object 'csv_proc' is not defined in app.py."
        assert hasattr(app, 'xml_proc'), "The object 'xml_proc' is not defined in app.py."
