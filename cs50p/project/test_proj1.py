import proj1
import pytest
from unittest.mock import patch

# Mocking generate_integer function
def mock_generate_integer(n):
    # Return a predictable value for testing
    return 3

def mock_input_six(prompt):
    return '6'

def mock_input_zero(prompt):
    return '0'

def mock_input_nine(prompt):
    return '9'

def mock_input_one(prompt):
    return '1'

@patch('proj1.generate_integer', side_effect=mock_generate_integer)
@patch('builtins.input', side_effect=mock_input_six)
def test_practice_arithmetic_addition(mock_input_six, mock_generate_integer):
    # Testing practice_arithmetic function for addition
    assert proj1.practice_arithmetic(1, '+') == 10

@patch('proj1.generate_integer', side_effect=mock_generate_integer)
@patch('builtins.input', side_effect=mock_input_zero)
def test_practice_arithmetic_subtraction(mock_input_zero, mock_generate_integer):
    # Testing practice_arithmetic function for subtraction
    assert proj1.practice_arithmetic(1, '-') == 10

@patch('proj1.generate_integer', side_effect=mock_generate_integer)
@patch('builtins.input', side_effect=mock_input_nine)
def test_practice_arithmetic_multiplication(mock_input_nine, mock_generate_integer):
    # Testing practice_arithmetic function for multiplication
    assert proj1.practice_arithmetic(1, '*') == 10

@patch('proj1.generate_integer', side_effect=mock_generate_integer)
@patch('builtins.input', side_effect=mock_input_one)
def test_practice_arithmetic_division(mock_input_one, mock_generate_integer):
    # Testing practice_arithmetic function for division
    assert proj1.practice_arithmetic(1, '/') == 10
