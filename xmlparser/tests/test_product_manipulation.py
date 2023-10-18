import pytest
from unittest.mock import patch, Mock
from parser.product_manipulation import (
    increase_prices,
    rename_category,
    remove_products,
    generate_reports,
    display_categories,
    generate_report_table,
    print_report_table,
)
from parser.customExceptions import (
    IncreasePriceException,
    CategoryNotFoundException,
    EmptyCategoryNameException,
    InvalidRatingException,
    ReportGenerationException,
)

class TestProductManipulation:
    @patch('parser.utility_functions.get_user_input', side_effect=['Electronics', '10'])
    def test_increase_prices(self, mock_user_input):
        products = [{"category": "Electronics", "price": 100.0}]
        result = increase_prices(products)
        assert result[0]['price'] == 110.0

    @patch('parser.utility_functions.get_user_input', side_effect=['NonexistentCategory', '10'])
    def test_increase_prices_category_not_found(self, mock_user_input):
        products = [{"category": "Electronics", "price": 100.0}]
        with pytest.raises(CategoryNotFoundException):
            increase_prices(products)

    @patch('parser.utility_functions.get_user_input', side_effect=['Electronics', 'NewElectronics'])
    def test_rename_category(self, mock_user_input):
        products = [{"category": "Electronics", "price": 100.0}]
        result = rename_category(products)
        assert result[0]['category'] == 'NewElectronics'

    @patch('parser.utility_functions.get_user_input', side_effect=['NonexistentCategory', 'NewCategory'])
    def test_rename_category_category_not_found(self, mock_user_input):
        products = [{"category": "Electronics", "price": 100.0}]
        with pytest.raises(CategoryNotFoundException):
            rename_category(products)

    @patch('parser.utility_functions.get_user_input', return_value='4.0')
    def test_remove_products(self, mock_user_input):
        products = [{"category": "Electronics", "price": 100.0, "rating": 5.0}]
        result = remove_products(products)
        assert not result

    @patch('parser.utility_functions.get_user_input', return_value='invalid_rating')
    def test_remove_products_invalid_rating(self, mock_user_input):
        products = [{"category": "Electronics", "price": 100.0, "rating": 5.0}]
        with pytest.raises(InvalidRatingException):
            remove_products(products)

    def test_generate_reports(self, capsys):
        products = [{"category": "Electronics", "price": 100.0}]
        generate_reports(products)
        captured = capsys.readouterr()
        assert "Electronics" in captured.out

    def test_generate_reports_exception(self):
        with patch('product_manipulation.generate_report_table', side_effect=Exception('Test')):
             result= generate_reports([])
        assert result == None

    def test_display_categories(self, capsys):
        categories = ['Electronics', 'Clothing']
        display_categories(categories)
        captured = capsys.readouterr()
        assert "Electronics" in captured.out
        assert "Clothing" in captured.out

    def test_generate_report_table(self):
        products = [{"category": "Electronics", "price": 100.0}]
        result = generate_report_table(products)
        assert result.field_names == ["Category", "Total Products by Category", "Total Price by Category"]

    def test_generate_report_table_empty(self):
        result = generate_report_table([])
        assert result is None

    def test_print_report_table(self, capsys):
        table = Mock()
        print_report_table(table)
        captured = capsys.readouterr()
        assert str(table) in captured.out

    def test_print_report_table_empty(self, capsys):
        print_report_table(None)
        captured = capsys.readouterr()
        assert "No products found" in captured.out
