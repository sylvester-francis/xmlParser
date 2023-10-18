'''
This module contains the utility functions
(1). return_args
(2). return_min_max_ratings
(3). get_user_input
(4). check_file_exists

Author: Sylvester Ranjith Francis
Date created : 10/15/2023
Last modified by: Sylvester Ranjith Francis
last modified date: 10/15/2023
'''
import os,argparse

class ArgumentParserWrapper:
    """Wrapper class for ArgumentParser to enable easier testing."""
    @staticmethod
    def create_parser():
        parser = argparse.ArgumentParser(description="XML Product Data parser")
        parser.add_argument('filepath', type=str, help="Path to the XML file")
        return parser

# Function to parse command-line arguments and return them
def return_args(parser=None, args=None):
    """Parse command-line arguments and return them."""
    if parser is None:
        parser = ArgumentParserWrapper.create_parser()
    parsed_args = parser.parse_args(args)
    return parsed_args

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

def check_file_exists(filepath):
    """Check if the specified file exists."""
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"The specified file is not found: {filepath}")

def return_file_path(directory='../output', filename='outputFile.xml'):
    try:
        filepath = os.path.join(directory, filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        return filepath
    except FileNotFoundError as e:
        raise e
    except Exception as e:
        raise FileNotFoundError(f"An exception occurred during file path retrieval: {type(e).__name__} - {e}")
