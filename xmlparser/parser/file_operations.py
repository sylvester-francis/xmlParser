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
from utility_functions import return_file_path

def read_file(filepath):
    try:
        # Check if the specified file exists
        if not os.path.isfile(filepath):
            # Raise an error if the file is not found
            raise FileNotFoundError(f"The specified file is not found: {filepath}")
        # If the file exists, return the file path
        return filepath
    except Exception as e:
        # Handle any other exceptions that might occur
        print(f"An exception occurred while trying to find the file: {type(e).__name__} : Error message - {e}")
        # Re-raise the exception to propagate it further
        raise

def save_changes(products):
    # Get command-line arguments
    filePath = return_file_path()
    # Create the root element for the XML tree
    root = ET.Element('products')
    # Iterate over each product in the list of products and add them to the XML tree
    for product in products: 
        # Create an element for each product with its attributes   
        product_elem = ET.Element('product', category=product['category'])
        name_elem = ET.Element('name')
        name_elem.text = product['name']
        price_elem = ET.Element('price')
        price_elem.text = str(product['price'])
        rating_elem = ET.Element('rating')
        rating_elem.text = str(product['rating'])
        # Append child elements to the product element
        product_elem.append(name_elem)
        product_elem.append(price_elem)
        product_elem.append(rating_elem)
        # Append the product element to the root
        root.append(product_elem)
    # Create an ElementTree with the root element    
    tree = ET.ElementTree(root)
    try:
        tree.write(filePath)
    # Write the XML tree to the specified file
    except ET.ParseError as e:
        # Handle parsing errors
        print(f"An exception occured while trying to save the file: {type(e).__name__} : Error message - {e}")
        # Re-raise the exception to propagate it further
        raise
