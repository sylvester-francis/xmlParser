from argparse import Namespace
import os
import pytest
from unittest.mock import patch
from parser.utility_functions import return_args,return_file_path,return_min_max_rating

def test_return_args():
    with patch('argparse.ArgumentParser.parse_args', return_value=Namespace(filepath='/path/to/xml/file.xml')):
        args = return_args()
        assert args.filepath == '/path/to/xml/file.xml'

def test_return_file_path():
    expected_directory = '../output'
    expected_filename = 'outputFile.xml'
    expected_filepath = os.path.join(expected_directory, expected_filename)
    with pytest.MonkeyPatch.context() as m:
        m.setattr(os, 'makedirs', lambda x: None)
        result = return_file_path()
    assert result == expected_filepath

def test_return_min_max_rating():
    min_rating, max_rating = return_min_max_rating()
    assert 0 <= min_rating <= 5
    assert 0 <= max_rating <= 5
    assert min_rating <= max_rating

