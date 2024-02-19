import pytest

from um import count


def test_um():
    assert count("um, hello, um, world") == 2
    assert count("yummy") == 0
