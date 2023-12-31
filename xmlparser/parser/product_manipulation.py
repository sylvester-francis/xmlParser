'''
This module contains the functions related to product manipulation
(1). increase_prices
(2). rename_category
(3). remove_products
(4). generate_reports

Author: Sylvester Ranjith Francis
Date created : 10/15/2023
Last modified by: Sylvester Ranjith Francis
last modified date: 10/17/2023
'''


from prettytable import PrettyTable 
# Import utility function for min and max ratings
from utility_functions import return_min_max_rating ,get_user_input 
from customExceptions import IncreasePriceException,CategoryNotFoundException,EmptyCategoryNameException,InvalidRatingException,ReportGenerationException



def display_categories(existing_categories):
    """Display the existing categories to the user."""
    print("The following are the categories of products in the inventory")
    for index, category in enumerate(existing_categories):
        print(f'{index + 1}:{category}')

def increase_prices(products, user_input_function=get_user_input):
    try:
        # Extract the existing categories from the product data
        existing_categories = list(set(existing_category['category'] for existing_category in products))
        # Display the existing categories to the user
        display_categories(existing_categories)
        # Prompt the user to enter the category to increase prices
        user_category = user_input_function("Enter the category of the products to increase the price of: ")
        # Check if the entered category exists
        if user_category not in existing_categories:
            raise CategoryNotFoundException("Category does not exist")
        # Prompt the user to enter the percentage to increase the price by
        percentage = float(user_input_function("Enter the percentage to increase the price by: "))
        # Iterate through products and update prices for the specified category
        for product in products:
            if product['category'] == user_category:
                product['price'] = round(product['price'] + (product['price'] * percentage / 100), 2)
        return products
    except (CategoryNotFoundException, ValueError) as e:
        raise e
    except Exception as e:
        raise IncreasePriceException(f"An exception occurred during price increase: {type(e).__name__} - {e}")


def rename_category(products, user_input_function=get_user_input):
    try:
        # Extract the existing categories from the product data
        existing_categories = list(set(existing_category['category'] for existing_category in products))
        # Display the existing categories to the user
        display_categories(existing_categories)
        # Prompt the user to enter the category to be renamed
        user_category = user_input_function("Enter the category to be renamed: ")
        # Check if the entered category exists
        if user_category not in existing_categories:
            raise CategoryNotFoundException("Category does not exist")
        # Prompt the user to enter the new name for the category
        new_user_category = user_input_function("Enter the name you want to give this category:")
        # Check if the new category name is not an empty string
        if not new_user_category:
            raise EmptyCategoryNameException("New Category cannot be an empty string")
        # Iterate through products and update the category name
        for product in products:
            if product['category'] == user_category:
                product['category'] = new_user_category
        # Return the updated products list
        return products
    except (CategoryNotFoundException, EmptyCategoryNameException) as e:
        raise e
    except Exception as e:
        raise ValueError(f"An exception occurred during category renaming: {type(e).__name__} - {e}")


def remove_products(products, user_input_function=get_user_input, rating_function=return_min_max_rating):
    try:
        min_rating, max_rating = rating_function()
        rating = float(user_input_function(f"Enter the rating below which all the products need to be removed (between {min_rating} and {max_rating}): "))
        if not (min_rating <= rating <= max_rating):
            raise InvalidRatingException(f"Value should be between {min_rating} and {max_rating}")
        products[:] = [product for product in products if product['rating'] >= rating]
        return products
    except (ValueError, InvalidRatingException) as e:
        raise e
    except Exception as e:
        raise ValueError(f"An exception occurred while trying to remove products: {type(e).__name__} - {e}")
    
def generate_report_table(products):
    """Generate a table with category, total products, and total price information."""
    try:
        if not products:
            return None  
        total_products_by_category = {}
        total_price_by_category = {}
        for product in products:
            category = product['category']
            if category not in total_products_by_category:
                total_products_by_category[category] = 0
                total_price_by_category[category] = 0
            total_products_by_category[category] += 1
            total_price_by_category[category] += product['price']
        # Create a PrettyTable for better presentation
        table = PrettyTable()
        table.field_names = ["Category", "Total Products by Category", "Total Price by Category"]
        # Add rows to the table with category, total products, and total price information
        for category in total_products_by_category:
            table.add_row([category, total_products_by_category[category], total_price_by_category[category]])
        return table
    except Exception as e:
        raise ReportGenerationException(f"An exception occurred during report generation: {type(e).__name__} - {e}")
    
def print_report_table(table):
    """Print the generated report table."""
    if table:
        print(table)
    else:
        print("No products found in inventory")

def generate_reports(products):
    try:
        table = generate_report_table(products)
        print_report_table(table)
    except ReportGenerationException as e:
        raise e
    except Exception as e:
        raise ReportGenerationException(f"An exception occurred during report generation: {type(e).__name__} - {e}")




