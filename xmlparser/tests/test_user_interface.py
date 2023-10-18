import pytest
from unittest.mock import patch
from parser.user_interface import MenuHandler, ExitHandler, quit, menu
from parser.customExceptions import CategoryNotFoundException

class TestMenuFunctionality:
    def test_display_menu_options(self, capsys):
        menu_handler = MenuHandler()
        menu_options = {"1": "Option 1", "2": "Option 2"}
        menu_handler.display_menu_options(menu_options)
        captured = capsys.readouterr()
        assert "Welcome user" in captured.out
        assert "Please select an option" in captured.out

    @patch('builtins.input', return_value='1')
    def test_get_user_choice(self, mock_input):
        menu_handler = MenuHandler()
        result = menu_handler.get_user_choice()
        assert result == '1'
                  
    @patch('builtins.input', return_value='3')
    def test_execute_menu_choice_remove_products(self, mock_input,capsys):
        menu_handler = MenuHandler()
        products = [{"name": "Product1", "price": 10.0, "category": "Electronics","rating":5}]
        menu_handler.execute_menu_choice("3", products)
        captured = capsys.readouterr()
        assert "Removing products based on rating" in captured.out
        assert "Products removed successfully" in captured.out

    @patch('builtins.input', return_value='4')
    def test_execute_menu_choice_generate_report_existing_file(self, mock_input,capsys):
        menu_handler = MenuHandler()
        products = [{"name": "Product1", "price": 10.0, "category": "Electronics","rating":5}]
        with patch('os.path.isfile', return_value=True):
            menu_handler.execute_menu_choice("4", products)
            captured = capsys.readouterr()
            assert "Generating reports from" in captured.out


    @patch('builtins.input', return_value='5')
    def test_execute_menu_choice_save_file(self, mock_input,capsys):
        menu_handler = MenuHandler()
        products = [{"name": "Product1", "price": 10.0, "category": "Electronics","rating":5}]
        menu_handler.execute_menu_choice("5", products)
        captured = capsys.readouterr()
        assert "Saving the file" in captured.out
        assert "File saved successfully" in captured.out

    @patch('builtins.input', return_value='6')
    def test_execute_menu_choice_exit_program(self, mock_input,capsys):
        menu_handler = MenuHandler()
        with patch.object(ExitHandler, 'exit_program') as mock_exit_program:
            menu_handler.execute_menu_choice("6", [])
            mock_exit_program.assert_called_once_with(menu_handler.exit_code)

    def test_handle_exception(self, capsys):
        menu_handler = MenuHandler()
        menu_handler.handle_exception(Exception("Test exception"))
        captured = capsys.readouterr()
        assert "An error occurred: Exception - Test exception" in captured.out

class TestExitHandler:
    def test_exit_program(self):
        with pytest.raises(SystemExit) as e:
            ExitHandler.exit_program(1)
        assert e.type == SystemExit
        assert e.value.code == 1

class TestQuitFunctionality:
    def test_quit(self):
        products = [{"name": "Product1", "price": 10.0, "category": "Electronics","rating":5}]
        with patch.object(ExitHandler, 'exit_program') as mock_exit_program:
                quit(products)
                mock_exit_program.assert_called_once()

class TestMenu:
    def test_menu_invalid_choice(self, capsys):
        products = [{"name": "Product1", "price": 10.0, "category": "Electronics","rating":5}]
        with patch('builtins.input', return_value='invalid'):
            menu(products)
            captured = capsys.readouterr()
            assert "Invalid input. Please select a valid option" in captured.out

