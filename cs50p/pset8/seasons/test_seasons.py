import seasons
import pytest


def test_age():
    assert seasons.sing("525600") == "five hundred twenty-five thousand, six hundred"


def test_format():
    with pytest.raises(ValueError):
        seasons.get_age("1989-12")
