import seasons
import pytest


def test_age():
    assert  age("525600") == "Five hundred twenty-five thousand, six hundred minutes"


def test_format():
    with pytest.raises(ValueError):
        main("1989-12")
