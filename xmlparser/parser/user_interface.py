'''
This module contains the code for the interactive Cli menu 
(1). menu
(2). quit

Author: Sylvester Ranjith Francis
Date created : 10/15/2023
Last modified by: Sylvester Ranjith Francis
last modified date: 10/15/2023
'''

import os,sys
# Importing functions from other modules
from product_manipulation import increase_prices, rename_category, remove_products, generate_reports
from file_operations import save_changes
from utility_functions import return_file_path
from xml_operations import parse_XML


class MenuHandler:
    """Handler for menu actions and external dependencies."""
    def __init__(self):
        self.exit_handler = ExitHandler()
        self.exit_code = 1 

    def display_menu_options(self, menu_options):
        print("**********************************************************************************")
        print("Welcome user")
        print("**********************************************************************************")
        print("Please select an option (Enter a number 1-6)")
        for key, value in menu_options.items():
            print(f"{key}:{value}")

    def get_user_choice(self):
        return input("> ")

    def handle_invalid_choice(self):
        print("Invalid input. Please select a valid option")

    def execute_menu_choice(self, choice, products):
        if choice == "1":
            print("Increasing prices")
            updated_products = increase_prices(products)
            if updated_products:
                save_changes(updated_products)
                print("Prices increased successfully.")
            else:
                save_changes(products)
                print("No products to update.")
        elif choice == "2":
            print("Renaming categories")
            renamed_products = rename_category(products)
            if renamed_products:
                save_changes(renamed_products)
                print("Categories renamed successfully.")
            else:
                save_changes(products)
                print("No categories to rename.")
        elif choice == "3":
            print("Removing products based on rating")
            products_after_removal = remove_products(products)
            if products_after_removal:
                save_changes(products_after_removal)
                print("Products removed successfully.")
            else:
                save_changes(products)
                print("No products to remove.")
        elif choice == "4":
            output_file_path = return_file_path()
            print(os.path.isfile(output_file_path))
            if os.path.isfile(output_file_path):
                print(f"Generating reports from {output_file_path}")
                parsed_products = parse_XML(output_file_path)
                generate_reports(parsed_products)
            else:    
                generate_reports(products)
                print(f'No changes detected,using original file')
        elif choice == "5":
            print("Saving the file")
            save_changes(products)
            print("File saved successfully.")
        elif choice == "6":
            print("Exiting... Goodbye")
            self.exit_handler.exit_program(self.exit_code)

    def handle_exception(self, e):
        print(f"An error occurred: {type(e).__name__} - {e}")

class ExitHandler:
    """Handler for program exit actions."""
    @staticmethod
    def exit_program(exit_code=1):
        sys.exit(exit_code)

def quit(products, exit_handler=None):
    """Save changes and exit the program."""
    if exit_handler is None:
        exit_handler = ExitHandler()
    save_changes(products)
    exit_handler.exit_program()   

def menu(products, menu_handler=None):
    try:
        if menu_handler is None:
            menu_handler = MenuHandler()
        menu_options = {
            "1": "Increase prices",
            "2": "Rename categories",
            "3": "Remove products",
            "4": "Generate report",
            "5": "Save the file",
            "6": "Exit"
        }
        menu_handler.display_menu_options(menu_options)
        choice = menu_handler.get_user_choice()
        if choice not in menu_options:
            menu_handler.handle_invalid_choice()
            return
        menu_handler.execute_menu_choice(choice, products)
    except Exception as e:
        menu_handler.handle_exception(e)
    menu(products, menu_handler)


