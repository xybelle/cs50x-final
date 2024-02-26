import game
import pytest
from unittest.mock import patch


def test_practice_addition():
    # Mocking input to provide correct answers
    with patch('builtins.input', side_effect=['4','6', '8', '2', '5', '7', '9', '1', '3', '0']):
        assert game.practice_addition(1) == 10
