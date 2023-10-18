'''
This module contains the utility functions
(1). return_args
(2). return_min_max_ratings

Author: Sylvester Ranjith Francis
Date created : 10/15/2023
Last modified by: Sylvester Ranjith Francis
last modified date: 10/15/2023
'''
import os,argparse


# Function to parse command-line arguments and return them
def return_args():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="XML Product Data parser")
    # Add a positional argument for the file path
    parser.add_argument('filepath', type=str, help="Please provide the path to the file containing the xml product data")
    # Parse the command-line arguments
    args = parser.parse_args()
    # Return the parsed arguments
    return args
def return_file_path():
    # Initialising a variable directory to point to a directory called output at the root of the project
    directory = '../output'
    # Initialising output filename
    filename = 'outputFile.xml'
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filename)
    return filepath

# Function to return the minimum and maximum rating values
def return_min_max_rating():
    # Set the minimum rating value
    min_rating = 0
    # Set the maximum rating value
    max_rating = 5
    # Return the minimum and maximum rating values as a tuple
    return min_rating, max_rating

def get_user_input(prompt):
    """Get user input with a specified prompt."""
    return input(prompt)
