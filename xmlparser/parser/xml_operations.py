'''
This module contains the function to perform the xml parsing

Author: Sylvester Ranjith Francis
Date created : 10/15/2023
Last modified by: Sylvester Ranjith Francis
last modified date: 10/17/2023
'''
import xml.etree.ElementTree as ET
from customExceptions import XMLParsingException

# Function to parse an XML product element and extract product data
def parse_product_element(product):
    """Parse an XML 'product' element and return product data."""
    try:
        category = product.get('category')
        name = product.find('name').text
        price = float(product.find('price').text)
        rating = float(product.find('rating').text)
        return {'category': category, 'name': name, 'price': price, 'rating': rating}
    except Exception as e:
        raise XMLParsingException(f"An exception occurred while parsing a 'product' element: {type(e).__name__} - {e}")

# Function to parse an XML file and form product data list
def parse_XML(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        products = []
        for product_element in root.findall('product'):
            product_data = parse_product_element(product_element)
            products.append(product_data)
        return products
    except XMLParsingException as e:
        raise e
    except Exception as e:
        raise XMLParsingException(f"An exception occurred during XML parsing: {type(e).__name__} - {e}")

