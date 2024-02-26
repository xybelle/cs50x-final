import game
import pytest
from unittest.mock import patch, MagicMock

# Mocking generate_integer function
def mock_generate_integer(n):
    # Return a predictable value for testing
    return 1


@patch('game.generate_integer', side_effect=mock_generate_integer)
@patch('builtins.input', side_effect=['2', '3', '4', '5', '6', '7', '8', '9', '10', '11'
                                      '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'
                                      '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])
def test_practice_addition(mock_input, mock_generate_integer):
    assert game.practice_addition(1) == 10
