import pytest
from parser.xml_operations import parse_XML 
import xml.etree.ElementTree as ET

sample_xml_content = """
<products>
    <product category="Electronics">
        <name>Laptop</name>
        <price>1000.0</price>
        <rating>4.5</rating>
    </product>
    <product category="Books">
        <name>Python Crash Course</name>
        <price>29.99</price>
        <rating>5.0</rating>
    </product>
</products>
"""

def test_parse_XML_valid_xml(tmp_path):
    xml_file_path = tmp_path / "test.xml"
    with open(xml_file_path, "w") as xml_file:
        xml_file.write(sample_xml_content)
    result = parse_XML(xml_file_path)
    expected_result = [
        {'category': 'Electronics', 'name': 'Laptop', 'price': 1000.0, 'rating': 4.5},
        {'category': 'Books', 'name': 'Python Crash Course', 'price': 29.99, 'rating': 5.0}
    ]
    assert result == expected_result

def test_parse_XML_invalid_xml(tmp_path):
    invalid_xml_content = "Invalid XML content"
    xml_file_path = tmp_path / "invalid.xml"
    with open(xml_file_path, "w") as xml_file:
        xml_file.write(invalid_xml_content)
    with pytest.raises(Exception):
        parse_XML(xml_file_path)


