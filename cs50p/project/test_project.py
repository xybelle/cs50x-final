import project
from unittest.mock import patch

# Mocking generate_integer function
def mock_generate_integer(n):
    # Return a predictable value for testing
    return 1


def mock_input(prompt):
    return "2"


def mock_input_sub(prompt):
    return "0"


def mock_input_one(prompt):
    return "1"


@patch('project.generate_integer', side_effect=mock_generate_integer)
@patch('builtins.input', side_effect=mock_input)
def test_practice_addition(mock_input, mock_generate_integer):
    assert project.practice_addition(2) == 10


@patch('project.generate_integer', side_effect=mock_generate_integer)
@patch('builtins.input', side_effect=mock_input_sub)
def test_practice_subtraction(mock_input_sub, mock_generate_integer):
    assert project.practice_subtraction(2) == 10


@patch('project.generate_integer', side_effect=mock_generate_integer)
@patch('builtins.input', side_effect=mock_input_one)
def test_practice_multi(mock_input_one, mock_generate_integer):
    assert project.practice_multiplication(2) == 10


@patch('project.generate_integer', side_effect=mock_generate_integer)
@patch('builtins.input', side_effect=mock_input_one)
def test_practice_div(mock_input_one, mock_generate_integer):
    assert project.practice_division(2) == 10
