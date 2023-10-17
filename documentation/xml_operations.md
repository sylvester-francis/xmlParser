# XML Operations Module

Author
------
Sylvester Ranjith Francis

Date Created
-------------
10/15/2023

Last Modified By
-----------------
Sylvester Ranjith Francis

Last Modified Date
-------------------
10/15/2023

## Functions
1. **parse_XML(xml_file)**
   - Parse the XML file using ElementTree.
   - Get the root element of the XML tree.
   - List to store product data.
   - Iterate through each 'product' element in the XML.
   - Extract information for each product and store it as a dictionary.
   - Append the product data dictionary to the list.
   - Return the list of product data.

## Exception Handling
- Handle exceptions that may occur during XML parsing.
- Print an error message if an exception occurs during parsing.
- Raise the exception to be caught by the calling code.
