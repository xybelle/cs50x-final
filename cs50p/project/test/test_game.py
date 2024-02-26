import game
import pytest
from unittest.mock import patch, MagicMock

# Mocking generate_integer function
def mock_generate_integer(n):
    # Return a predictable value for testing
    return 1


def test_practice_addition():
    # Patching generate_integer to always return 1
    with patch('game.generate_integer', side_effect=mock_generate_integer):
        # Providing known inputs to practice_addition
        result = game.practice_addition(1)

        # Since generate_integer always returns 1 and the correct answers are always 10,
        # the result should be 10
        assert result == 10
