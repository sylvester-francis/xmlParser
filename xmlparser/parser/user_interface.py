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
from product_manipulation import increase_price, rename_category, remove_products, generate_reports
from file_operations import save_changes
from utility_functions import return_file_path
from xml_operations import parse_XML

def quit(products):
    # Save changes to the XML file before exiting
    save_changes(products)
    # Exit the program with status code 1
    sys.exit(1)
    

def menu(products):
    try:
        # Define menu options as a dictionary
        menu_options = {
            "1": "Increase prices",
            "2": "Rename categories",
            "3": "Remove products",
            "4": "Generate report",
            "5": "Save the file",
            "6": "Exit"
        }
        # Display welcome message and menu options to the user
        print("**********************************************************************************")
        print("Welcome user")
        print("**********************************************************************************")
        print("Please select an option (Enter a number 1-6)")
        # Print each menu option with its corresponding number
        for key, value in menu_options.items():
            print(f"{key}:{value}")
        # Get user input for menu choice
        choice = input(">  ") 
        # Check if the user choice is valid
        if choice not in menu_options:
            print("Invalid input. Please select a valid option ")
            return
        # Execute the chosen action based on user input
        if choice == "1":
            print("Increasing prices")
            updated_products = increase_price(products)
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
            report_filepath = return_file_path()
            if os.path.isfile(report_filepath):
                print(f"Generating reports from {report_filepath}")
                parsed_products = parse_XML(report_filepath)
                generate_reports(parsed_products)
            else:
                print("No changes detected. Generating reports from input file.")
                generate_reports(products)
        elif choice == "5":
            print("Saving the file")
            save_changes(products)
            print("File saved successfully.")    
        elif choice == "6":
            print("Exiting... Goodbye")
            quit(products)
    except Exception as e:
        print(f"An error occurred: {type(e).__name__} - {e}")
    # Recursive call to keep the menu running
    menu(products)
