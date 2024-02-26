import game
import pytest
from unittest.mock import patch

# Mocking input function for user input simulation
def mock_input(prompt):
    # Return a predictable value for testing
    return '5'  # Sample input for testing

@patch('builtins.input', side_effect=mock_input)
def test_practice_operation_addition(mock_input):
    # Testing practice_operation function for addition
    assert game.practice_operation(1, '+') == 10  # Assuming 10 correct answers for level 1

@patch('builtins.input', side_effect=mock_input)
def test_practice_operation_subtraction(mock_input):
    # Testing practice_operation function for subtraction
    assert game.practice_operation(1, '-') == 10  # Assuming 10 correct answers for level 1
