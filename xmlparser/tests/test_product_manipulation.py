import pytest
from prettytable import PrettyTable 
from unittest.mock import patch
from parser.utility_functions import return_min_max_rating
from parser.product_manipulation import increase_price,rename_category,remove_products,generate_reports

# Mock product data for testing
mock_products = [{'category': 'Electronics', 'name': 'Laptop', 'price': 1000.0, 'rating': 4.5}]
min_rating, max_rating = return_min_max_rating()
gen_mock_products = [
    {'category': 'Electronics', 'name': 'Laptop', 'price': 1000.0, 'rating': 4.5},
    {'category': 'Books', 'name': 'Book', 'price': 20.0, 'rating': 4.0},
    {'category': 'Electronics', 'name': 'Smartphone', 'price': 800.0, 'rating': 4.2}
]


def test_increase_price(monkeypatch):
    inputs = iter(['Electronics', '10'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    updated_products = increase_price(mock_products)
    assert updated_products[0]['price'] == 1100.0

def test_increase_price_invalid_category(capsys, monkeypatch):
    mock_products = [{'category': 'Electronics', 'name': 'Laptop', 'price': 1000.0, 'rating': 4.5}]
    inputs = iter(['InvalidCategory', '10'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with patch('builtins.print') as mock_print:
        updated_products = increase_price(mock_products)
    assert "Category does not exist" in mock_print.call_args_list[-1][0][0]
    assert updated_products == None

def test_increase_price_exception(capsys, monkeypatch):
    mock_products = [{'category': 'Electronics', 'name': 'Laptop', 'price': 1000.0, 'rating': 4.5}]
    inputs = iter(['Electronics', '10'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with patch('builtins.print') as mock_print:
        with patch('builtins.input', side_effect=ValueError('Test exception')):
            updated_products = increase_price(mock_products)
    assert updated_products == None



def test_rename_category(monkeypatch):
    inputs = iter(['Electronics', 'NewElectronics'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    updated_products = rename_category(mock_products)
    assert updated_products[0]['category'] == 'NewElectronics'

def test_rename_category_nonexistent_category(monkeypatch, capsys):
    inputs = iter(['NoCategory', 'NewCategory'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    updated_products = rename_category(mock_products)
    captured = capsys.readouterr()
    assert "Category does not exist" in captured.out
    assert updated_products == None


def test_remove_products(monkeypatch):
    inputs = iter(['3.0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    updated_products = remove_products(mock_products)
    assert not any(product['rating'] < 3.0 for product in updated_products)

def test_remove_products_out_of_range(monkeypatch, capsys):
    inputs = iter(['6.0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(ValueError, match="Value should be between 0 and 5"):
        remove_products(mock_products)
    captured = capsys.readouterr()
    assert "An exception occurred while trying to remove products" in captured.out

def test_remove_products_invalid_input(capsys, monkeypatch):
    mock_products = [{'category': 'Electronics', 'name': 'Laptop', 'price': 1000.0, 'rating': 4.5}]
    inputs = iter(['InvalidRating'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    updated_products = remove_products(mock_products)
    captured = capsys.readouterr()
    assert "An exception occurred while trying to remove products" in captured.out

def test_remove_products_exception(capsys, monkeypatch):
    mock_products = [{'category': 'Electronics', 'name': 'Laptop', 'price': 1000.0, 'rating': 4.5}]

    inputs = ['4.0']
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with patch('builtins.print') as mock_print:
        with patch('builtins.input', side_effect=ValueError('Test exception')):
            updated_products = remove_products(mock_products)

    assert "An exception occurred while trying to remove products" in mock_print.call_args_list[-1][0][0]


def test_generate_reports(capsys):
    generate_reports(gen_mock_products)
    captured = capsys.readouterr()
    
    # Check if the generated report contains expected information
    assert "Category" in captured.out
    assert "Total Products by Category" in captured.out
    assert "Total Price by Category" in captured.out

def test_generate_reports_empty(capsys):
    generate_reports([])
    captured = capsys.readouterr()
    # Check if the message for no products is printed
    assert "No products found in inventory" in captured.out
