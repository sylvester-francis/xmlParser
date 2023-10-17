# Product Manipulation Module

Author
------
Sylvester Ranjith Francis

Date Created
-------------
10/15/2023

Last Modified By
-----------------
Sylvester Ranjith Francis

Last Modified Date
-------------------
10/15/2023

## Functions
1. **increase_price(products)**
   - Extract existing categories from the product data.
   - Display categories to the user.
   - Prompt the user to enter the category to increase prices.
   - Check if the entered category exists.
   - Prompt the user to enter the percentage to increase the price by.
   - Iterate through products and update prices for the specified category.
   - Return the updated products list.

2. **rename_category(products)**
   - Extract existing categories from the product data.
   - Display existing categories to the user.
   - Prompt the user to enter the category to be renamed.
   - Check if the entered category exists.
   - Prompt the user to enter the new name for the category.
   - Check if the new category name is not an empty string.
   - Iterate through products and update the category name.
   - Return the updated products list.

3. **remove_products(products)**
   - Prompt the user to enter the rating below which products should be removed.
   - Check if the entered rating is within the specified range.
   - Iterate through products and remove those below the specified rating.
   - Return the updated products list.

4. **generate_reports(products)**
   - Check if there are no products in the inventory.
   - Dictionaries to store total products and total price for each category.
   - Iterate through each product in the list.
   - Extract the category of the product.
   - Update the total products and total price for the category.
   - Create a PrettyTable for better presentation.
   - Add rows to the table with category, total products, and total price information.
   - Print the generated table.

## Functions Imported
- **return_min_max_rating()** from `utility_functions`
- **PrettyTable** from `prettytable`
