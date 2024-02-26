import proj1
import pytest
from unittest.mock import patch

# Mocking generate_integer function
def mock_generate_integer(n):
    # Return a predictable value for testing
    return 3

# Parameterized input values for testing
input_values = ['6', '0', '9', '1']
expected_results = [10, 10, 10, 10]

@pytest.mark.parametrize("input_value, expected_result", zip(input_values, expected_results))
@patch('proj1.generate_integer', side_effect=mock_generate_integer)
def test_practice_arithmetic_addition(mock_generate_integer, input_value, expected_result):
    
    # Testing practice_arithmetic function for addition
    assert proj1.practice_arithmetic(1, '+') == expected_result

