# Welcome to XML Parser Tool’s documentation!

## main.py Module

A basic XML parser tool which parses an XML file containing product data, manipulates the data, and saves the results back to the XML file and generates reports from the XML file.

### Author
Sylvester Ranjith Francis

### Date Created
10/13/2023

### Last Modified By
Sylvester Ranjith Francis

### Last Modified Date
10/13/2023

### Usage
Navigate to the `parser` directory and run:

```bash
python main.py <filename.xml>
```
### Example usage
```bash
python main.py ../sampleXML.xml
```
## Description

This module (`main.py`) serves as the entry point for the XML parser tool. It performs the following steps:

1. Import utility functions from `utility_functions`.
2. Import functions from other modules, including `file_operations`, `xml_operations`, and `user_interface`.
3. If executed as the main script (`__name__ == '__main__'`):
    a. Get command-line arguments using `return_args` from `utility_functions`.
    b. Read the specified XML file using `read_file` from `file_operations`.
    c. Check if the file is not found and display a message if needed.
    d. If the file is found, extract product data using `parse_XML` from `xml_operations`.
    e. Display a menu for user options using `menu` from `user_interface`.

### Command-line Usage

Navigate to the `parser` directory and run the following command:

```bash
python main.py <filename.xml>
```