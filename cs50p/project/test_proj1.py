import proj1
import pytest
from unittest.mock import patch

# Mocking generate_integer function
def mock_generate_integer(n):
    # Return a predictable value for testing
    return 1

# Mocking input function for user input simulation
def mock_input(prompt):
    # Return a predictable value for testing
    return '2'  # Sample input for testing

# Mocking input function for user input simulation
def mock_input_zero(prompt):
    # Return a predictable value for testing
    return '0'  # Sample input for testing

@patch('proj1.generate_integer', side_effect=mock_generate_integer)
@patch('builtins.input', side_effect=mock_input)
def test_practice_arithmetic_addition(mock_input, mock_generate_integer):
    # Testing practice_arithmetic function for addition
    assert proj1.practice_arithmetic(1, '+') == 10  # Assuming 10 correct answers for level 1

@patch('proj1.generate_integer', side_effect=mock_generate_integer)
@patch('builtins.input', side_effect=mock_input_zero)
def test_practice_arithmetic_subtraction(mock_input_zero, mock_generate_integer):
    # Testing practice_arithmetic function for subtraction
    assert proj1.practice_arithmetic(1, '-') == 10  # Assuming 10 correct answers for level 1
