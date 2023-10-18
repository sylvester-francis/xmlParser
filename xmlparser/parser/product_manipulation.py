'''
This module contains the functions related to product manipulation
(1). increase_price
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
from utility_functions import return_min_max_rating  
# Get the min and max ratings using the utility function
min_rating, max_rating = return_min_max_rating()


class IncreasePriceException(Exception):
    """Exception raised for errors during the increase price process."""
    pass

class CategoryNotFoundException(Exception):
    """Exception raised when the specified category is not found."""
    pass

def increase_prices(products, user_category, percentage):
    try:
        # Extract the existing categories from the product data
        existing_categories = list(set(existing_category['category'] for existing_category in products))
        # Check if the entered category exists
        if user_category not in existing_categories:
            raise CategoryNotFoundException("Category does not exist")
        # Iterate through products and update prices for the specified category
        for product in products:
            if product['category'] == user_category:
                product['price'] = round(product['price'] + (product['price'] * percentage / 100), 2)
        # Return the updated products list
        return products
    except Exception as e:
        raise IncreasePriceException(f"An exception occurred while trying to increase the price: {type(e).__name__} : Error message - {e}")

def rename_category(products):
    try:
        # Extract the existing categories from the product data
        existing_categories = list(set(existing_category['category'] for existing_category in products))
        # Display the existing categories to the user
        print("The following are the categories of products in the inventory")
        for index, category in enumerate(existing_categories):
            print(f'{index+1}:{category}')
        # Prompt the user to enter the category to be renamed
        user_category = input("Enter the category to be renamed: ")
        # Check if the entered category exists
        if user_category not in existing_categories:
            print("Category does not exist")
            return
        # Prompt the user to enter the new name for the category
        new_user_category = input("Enter the name you want to give this category:")
        # Check if the new category name is not an empty string
        if not new_user_category:
            raise ValueError("New Category cannot be an empty string")
        # Iterate through products and update the category name
        for product in products:
            if product['category'] == user_category:
                product['category'] = new_user_category
        # Return the updated products list
        return products
    except Exception as e:
        # Handle exceptions that may occur during category renaming
        print(f"An exception occurred while trying to rename the category: {type(e).__name__} : Error message - {e}")
        # Raise the exception to be caught by the calling code
        raise

def remove_products(products):
    try:
        # Prompt the user to enter the rating below which products should be removed
        rating = float(input("Enter the rating below which all the products need to be removed:"))
        # Check if the entered rating is within the specified range
        if not (min_rating <= rating <= max_rating):
            raise ValueError(f"Value should be between {min_rating} and {max_rating}")
        # Iterate through products and remove those below the specified rating
        for product in products:
            if product['rating'] < rating:
                products.remove(product)
        # Return the updated products list
        return products
    except ValueError as e:
        # Handle the specific ValueError for invalid input
        print(f"An exception occurred while trying to remove products: {type(e).__name__} : Error message - {e}")
        # Raise the exception to be caught by the calling code
        raise
def generate_reports(products):
    try:
        # Check if there are no products in the inventory
        if not products:
            print("No products found in inventory")
            return
        # Dictionaries to store total products and total price for each category
        total_products_by_category = {}
        total_price_by_category = {}
        # Iterate through each product in the list
        for product in products:
            # Extract the category of the product
            category = product['category']
            # Update the total products and total price for the category
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
        # Print the generated table
        print(table)
    except Exception as e:
        # Handle exceptions that may occur during report generation
        print(f"An exception occurred while trying to generate reports: {type(e).__name__} : Error message - {e}")
        # Raise the exception to be caught by the calling code
        raise

