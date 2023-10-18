import os
import xml.etree.ElementTree as ET
import pytest
from unittest.mock import patch
from parser.file_operations import read_file, save_changes
from parser.customExceptions import SaveChangesException, ReadFileException

class TestFileOperations:
    # Test read_file function
    def test_read_file_valid(self, tmp_path):
        sample_xml_content = "<products></products>"
        sample_xml_file = tmp_path / 'sample.xml'
        sample_xml_file.write_text(sample_xml_content)
        result = read_file(str(sample_xml_file))
        assert result == str(sample_xml_file)

    def test_read_file_invalid_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            read_file('nonexistent_file.xml')

    def test_read_file_invalid_exception(self, tmp_path):
        sample_xml_content = "<products></products>"
        sample_xml_file = tmp_path / 'sample.xml'
        sample_xml_file.write_text(sample_xml_content)
        with patch('parser.file_operations.check_file_exists', side_effect=Exception('Test')):
            with pytest.raises(Exception) as exc_info:
                read_file(str(sample_xml_file))
        assert 'An exception occurred during file reading: Exception' in str(exc_info.value)

    def test_save_changes_valid(self, tmp_path):
        products = [{"category": "Electronics", "name": "Laptop", "price": 1000.0, "rating": 4.5}]
        file_path = str(tmp_path / 'output.xml')
        save_changes(products, file_path)
        assert os.path.isfile(file_path)

    def test_save_changes_invalid_exception(self, tmp_path):
        products = [{"category": "Electronics", "name": "Laptop", "price": 1000.0, "rating": 4.5}]
        with patch('parser.file_operations.write_xml_tree', side_effect=Exception('Test')):
            with pytest.raises(Exception) as exc_info:
                save_changes(products)
        assert 'An exception occurred during save changes: Exception - Test' in str(exc_info.value)

    def test_save_changes_invalid_custom_exception(self, tmp_path):
        products = [{"category": "Electronics", "name": "Laptop", "price": 1000.0, "rating": 4.5}]
        with patch('parser.file_operations.write_xml_tree', side_effect=ET.ParseError('Test')):
            with pytest.raises(Exception) as exc_info:
                save_changes(products)
        assert 'An exception occurred during save changes: ParseError - Test' in str(exc_info.value)
