'''
A basic XML parser tool which parses an XML file containing product data, manipulates the data 
and saves the results back to the xml file and generates reports from the xml file

Author: Sylvester Ranjith Francis
Date created : 10/13/2023
Last modified by: Sylvester Ranjith Francis
last modified date: 10/13/2023
'''

# Import utility functions
from utility_functions import return_args
# Importing functions from other modules
from file_operations import read_file
from xml_operations import parse_XML
from user_interface import menu

if __name__ == '__main__':
    # Get arguments passed in command line arguments
    args = return_args()
    # Read the file specified in command line arguments
    xml_file = read_file(args.filepath)
    #Check if file is not found
    if not xml_file:
        print("The specified file path is not found")
    else:
        # Extract product data from given xml file
        products = parse_XML(xml_file)
        # Display a menu for user options
        menu(products)