import game
import pytest
from unittest.mock import patch

# Mocking generate_integer function
def mock_generate_integer(n):
    # Return a predictable value for testing
    return 1


def test_practice_addition(1):
    with patch('builtins.input', side_effect=['4', '6', '8', '2', '5', '7', '9', '1', '3', '0']):
        assert game.practice_addition(1) == 10
