import proj1
import pytest
from unittest.mock import patch

# Mocking generate_integer function
def mock_generate_integer(n):
    # Return a predictable value for testing
    return 3

# Define mock input function using pytest.fixture
@pytest.fixture
def mock_input(request):
    def mock_func(prompt):
        return {
            '6': '6',
            '0': '0',
            '9': '9',
            '1': '1'
        }[prompt]
    return mock_func

# Define test cases using parameterized testing
@pytest.mark.parametrize("mock_input_value, expected_result, operation", [
    ('6', 10, '+'),
    ('0', 10, '-'),
    ('9', 10, '*'),
    ('1', 10, '/')
])
def test_practice_arithmetic(mock_input, mock_generate_integer, mock_input_value, expected_result, operation):
    with patch('proj1.generate_integer', side_effect=mock_generate_integer), \
         patch('builtins.input', side_effect=mock_input(mock_input_value)):

        # Testing practice_arithmetic function for different scenarios
        assert proj1.practice_arithmetic(1, operation) == expected_result
