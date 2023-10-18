import pytest
from unittest.mock import patch
from parser.main import initial

def test_main_file_not_found(capsys):
    with patch('sys.argv', ['main.py', 'nonexistent.xml']):
        with pytest.raises(Exception) as exc_info:
             initial()
        assert 'The specified file is not found: nonexistent.xml' in str(exc_info.value)