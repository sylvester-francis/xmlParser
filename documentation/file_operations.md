# File Operations Module

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
1. **read_file(filepath)**
   - Check if the specified file exists.
   - Raise an error if the file is not found.
   - Return the file path if the file exists.

2. **save_changes(products)**
   - Get the file path using `return_file_path()`.
   - Create the root element for the XML tree.
   - Iterate over each product in the list of products and add them to the XML tree.
   - Create an ElementTree with the root element.
   - Write the XML tree to the specified file.
   - Output file is stored in ./output/ with the file name outputFile.xml

## Functions Imported
- **return_file_path()** from `utility_functions`
- **ET (xml.etree.ElementTree)** from `xml.etree.ElementTree`
