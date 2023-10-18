import os
import pytest
from unittest.mock import patch
from argparse import ArgumentParser
from parser.utility_functions import (
    return_args,
    return_min_max_rating,
    get_user_input,
    check_file_exists,
    return_file_path,
    ArgumentParserWrapper
)

class TestUtilityFunctions:
    def test_return_args(self):
        parser = ArgumentParserWrapper.create_parser()
        args = ['--filepath', 'test.xml']
        with pytest.raises(SystemExit) as e:
            return_args(parser=parser, args=args)
        assert e.value.code == 2

    def test_return_min_max_rating(self):
        result = return_min_max_rating()
        assert result == (0, 5)

    @patch('builtins.input', return_value='test_input')
    def test_get_user_input(self, mock_input):
        result = get_user_input('Enter something: ')
        assert result == 'test_input'

    def test_check_file_exists_file_found(self, tmp_path):
        test_file = tmp_path / 'test_file.txt'
        test_file.touch()
        result = check_file_exists(str(test_file))
        assert result is None

    def test_check_file_exists_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            check_file_exists('nonexistent_file.txt')

    def test_return_file_path(self, tmp_path):
        result = return_file_path(directory=str(tmp_path), filename='test_file.xml')
        os.path.isabs(result)

    def test_return_file_path_exception(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            return_file_path(directory='/nonexistent_directory', filename='test_file.xml')
