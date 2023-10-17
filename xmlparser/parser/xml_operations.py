'''
This module contains the function to perform the xml parsing

Author: Sylvester Ranjith Francis
Date created : 10/15/2023
Last modified by: Sylvester Ranjith Francis
last modified date: 10/15/2023
'''
import xml.etree.ElementTree as ET
# Function to parse an XML file and extract product data
def parse_XML(xml_file):
    try:
        # Parse the XML file using ElementTree
        tree = ET.parse(xml_file)

        # Get the root element of the XML tree
        root = tree.getroot()

        # List to store product data
        products = []

        # Iterate through each 'product' element in the XML
        for product in root.findall('product'):
            # Extract information for each product and store it as a dictionary
            product_data = {
                'category': product.get('category'),
                'name': product.find('name').text,
                'price': float(product.find('price').text),
                'rating': float(product.find('rating').text)
            }
            # Append the product data dictionary to the list
            products.append(product_data)
        # Return the list of product data
        return products

    except Exception as e:
        # Handle exceptions that may occur during XML parsing
        print(f"Error parsing the provided XML file: {type(e).__name__} : Error message - {e}")
        # Raise the exception to be caught by the calling code
        raise
