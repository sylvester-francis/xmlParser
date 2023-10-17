import os
import pytest
from parser.file_operations import read_file

# Test case for an existing file
def test_read_file_existing_file(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")

    # Call the read_file function
    result = read_file(str(test_file))

    # Check if the result is the expected file path
    assert result == str(test_file)

# Test case for a non-existing file
def test_read_file_non_existing_file(tmp_path):
    # Create a temporary directory
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()

    # Specify a file path that doesn't exist
    non_existing_file = test_dir / "non_existing_file.txt"

    # Call the read_file function, and it should raise FileNotFoundError
    with pytest.raises(FileNotFoundError):
        read_file(str(non_existing_file))

# Test case for handling other exceptions
def test_read_file_other_exceptions(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")

    # Call the read_file function with an invalid file path
    with pytest.raises(Exception):
        read_file("invalid_file_path")

