import re,pytest
import xml.etree.ElementTree as ET
from parser.xml_operations import parse_product_element, parse_XML
from parser.customExceptions import XMLParsingException

def test_parse_product_element():
    sample_product_element = ET.Element('product', category='Electronics')
    ET.SubElement(sample_product_element, 'name').text = 'Laptop'
    ET.SubElement(sample_product_element, 'price').text = '999.99'
    ET.SubElement(sample_product_element, 'rating').text = '4.5'
    result = parse_product_element(sample_product_element)
    expected_result = {'category': 'Electronics', 'name': 'Laptop', 'price': 999.99, 'rating': 4.5}
    assert result == expected_result

def test_parse_XML(tmp_path):
    sample_xml_content = """
    <products>
        <product category="Electronics">
            <name>Laptop</name>
            <price>999.99</price>
            <rating>4.5</rating>
        </product>
        <product category="Clothing">
            <name>T-shirt</name>
            <price>19.99</price>
            <rating>3.8</rating>
        </product>
    </products>
    """
    sample_xml_file = tmp_path / 'sample.xml'
    sample_xml_file.write_text(sample_xml_content)
    result = parse_XML(str(sample_xml_file))
    expected_result = [
        {'category': 'Electronics', 'name': 'Laptop', 'price': 999.99, 'rating': 4.5},
        {'category': 'Clothing', 'name': 'T-shirt', 'price': 19.99, 'rating': 3.8}
    ]
    assert result == expected_result

def test_parse_XML_exception_handling(tmp_path):
    sample_xml_content = "<invalid><tag></invalid>"
    sample_xml_file = tmp_path / 'invalid_sample.xml'
    sample_xml_file.write_text(sample_xml_content)
    with pytest.raises(Exception) as exc_info:
        parse_XML(str(sample_xml_file))

