import sys
import pytest
from unittest.mock import patch

from parser.user_interface import menu,quit

# Mock product data for testing
mock_products = [
    {'category': 'Electronics', 'name': 'Laptop', 'price': 1000.0, 'rating': 4.5},
    {'category': 'Books', 'name': 'Book', 'price': 20.0, 'rating': 4.0},
    {'category': 'Electronics', 'name': 'Smartphone', 'price': 800.0, 'rating': 4.2}
]
# Test menu with invalid user choice
def mock_input(choices):
    return lambda _: choices.pop(0)

def test_menu_invalid_choice(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', mock_input(["7"]))
    menu(mock_products)
    captured = capsys.readouterr()
    assert "Invalid input. Please select a valid option" in captured.out


def test_menu_exit(capsys):
    with patch('builtins.input', return_value="6"):
        with pytest.raises(SystemExit):
            menu(mock_products)
            
def test_quit(capsys, monkeypatch):
    monkeypatch.setattr(sys, 'exit', lambda code: None)
    with patch('parser.user_interface.save_changes') as mock_save_changes:
        quit(mock_products)
    # Ensure that the save_changes function was called with the correct argument
    mock_save_changes.assert_called_once_with(mock_products)
    # Check if the program would have exited with status code 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""

def test_quit_empty(capsys, monkeypatch):
    monkeypatch.setattr(sys, 'exit', lambda code: None)
    with patch('parser.user_interface.save_changes') as mock_save_changes:
        quit([])
    # Ensure that the save_changes function was called with the correct argument
    mock_save_changes.assert_called_once_with([])
    # Check if the program would have exited with status code 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
  