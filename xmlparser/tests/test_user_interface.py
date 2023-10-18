import sys
import os,pytest
from unittest.mock import patch
from parser.user_interface import menu, quit
from parser.product_manipulation import increase_price, rename_category, remove_products, generate_reports
from parser.file_operations import save_changes
from parser.utility_functions import return_file_path
from parser.xml_operations import parse_XML


@pytest.mark.parametrize("user_input, expected_output, mock_function, mock_function_args", [
    ("1", "Prices increased successfully.", increase_price, ([],)),
    ("2", "Categories renamed successfully.", rename_category, ([],)),
    ("3", "Products removed successfully.", remove_products, ([],)),
    ("4", "Generating reports", generate_reports, ([],)),
    ("5", "File saved successfully.", save_changes, ([],)),
    ("6", "Exiting... Goodbye", quit, ([],)),
    ("7", "Invalid input. Please select a valid option", None, None),
])
def test_menu(user_input, expected_output, mock_function, mock_function_args):
    products = [...]  # Your initial products list
    with patch('builtins.input', return_value=user_input), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        if mock_function:
            with patch(mock_function.__module__ + '.' + mock_function.__name__, return_value=mock_function_args[0]) as mock_function_patch:
                menu(products)
                mock_function_patch.assert_called_with(*mock_function_args)
        else:
            menu(products)

        output = mock_stdout.getvalue().strip()
        assert expected_output in output

def test_recursive_call():
    with patch('builtins.input', side_effect=["1", "6"]), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        menu([])
        output = mock_stdout.getvalue().strip()
        assert "Exiting... Goodbye" in output

if __name__ == '__main__':
    pytest.main()
