'''
This module contains all the file operations that are performed by this application, namely 
(1). read_file
(2). save_changes

Author: Sylvester Ranjith Francis
Date created : 10/15/2023
Last modified by: Sylvester Ranjith Francis
last modified date: 10/15/2023
'''

import os
# Importing etree module
import xml.etree.ElementTree as ET
# Importing utility functions
from utility_functions import return_file_path,check_file_exists
# Importing custom exceptions 
from customExceptions import SaveChangesException,ReadFileException


def read_file(filepath):
    try:
        # Check if the specified file exists
        check_file_exists(filepath)
        # If the file exists, return the file path
        return filepath

    except FileNotFoundError as e:
        # Raise specific exceptions for unit testing
        raise e
    except Exception as e:
        # Raise a generic exception with details for unit testing
        raise ReadFileException(f"An exception occurred during file reading: {type(e).__name__} - {e}")

def create_product_element(product):
    """Create an Element for a product with its attributes."""
    product_elem = ET.Element('product', category=product['category'])
    name_elem = ET.Element('name')
    name_elem.text = product['name']
    price_elem = ET.Element('price')
    price_elem.text = str(product['price'])
    rating_elem = ET.Element('rating')
    rating_elem.text = str(product['rating'])
    product_elem.append(name_elem)
    product_elem.append(price_elem)
    product_elem.append(rating_elem)
    return product_elem

def create_xml_tree(products):
    """Create an ElementTree with products as elements."""
    root = ET.Element('products')
    for product in products:
        product_elem = create_product_element(product)
        root.append(product_elem)
    return ET.ElementTree(root)

def write_xml_tree(tree, file_path):
    """Write the XML tree to the specified file path."""
    try:
        tree.write(file_path)
    except ET.ParseError as e:
        raise SaveChangesException(f"An exception occurred while trying to save the file: {type(e).__name__} : Error message - {e}")

def save_changes(products, file_path=None):
    try:
        # Get file path from the parameter or use a default value
        file_path = file_path or return_file_path()

        # Create an ElementTree with products as elements
        tree = create_xml_tree(products)

        # Write the XML tree to the specified file path
        write_xml_tree(tree, file_path)

    except SaveChangesException as e:
        # Raise specific exceptions for unit testing
        raise e
    except Exception as e:
        # Raise a generic exception with details for unit testing
        raise SaveChangesException(f"An exception occurred during save changes: {type(e).__name__} - {e}")