import game
from unittest.mock import patch

# Mocking generate_integer function
def mock_generate_integer(n):
    # Return a predictable value for testing
    return 1

# Mocking input function
def mock_input(prompt):
    # Return a predictable value for testing
    return "2"


# Mocking input function
def mock_input_sub(prompt):
    # Return a predictable value for testing
    return "0"


@patch('game.generate_integer', side_effect=mock_generate_integer)
@patch('builtins.input', side_effect=mock_input)
def test_practice_addition(mock_input, mock_generate_integer):
    assert game.practice_addition(2) == 10


@patch('game.generate_integer', side_effect=mock_generate_integer)
@patch('builtins.input', side_effect=mock_input_sub)
def test_practice_subtraction(mock_input, mock_generate_integer):
    assert game.practice_subtraction(2) == 10


@patch('game.generate_integer', side_effect=mock_generate_integer)
@patch('builtins.input', side_effect=mock_input_sub)
def test_practice_multi(mock_input, mock_generate_integer):
    assert game.practice_multi(2) == 10
