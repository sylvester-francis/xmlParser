# Utility Functions Module

## Author
Sylvester Ranjith Francis

## Date Created
10/15/2023

## Last Modified By
Sylvester Ranjith Francis

## Last Modified Date
10/15/2023

## Functions
1. **return_args()**
   - Create an ArgumentParser object.
   - Add a positional argument for the file path.
   - Parse the command-line arguments.
   - Return the parsed arguments.

2. **return_file_path()**
   - Initialize a variable `directory` to point to a directory called 'output' at the root of the project.
   - Initialize output filename.
   - If the directory does not exist, create it.
   - Create the file path by joining the directory and filename.
   - Return the file path.

3. **return_min_max_rating()**
   - Set the minimum rating value.
   - Set the maximum rating value.
   - Return the minimum and maximum rating values as a tuple.

## Exception Handling
- No explicit exception handling in these functions.
- Exceptions, if any, will propagate to the calling code.
