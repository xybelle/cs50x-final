from fuel import convert, gauge


def test_convert():
    assert convert("1/4") == 25
    assert convert("3/4") == 75


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(75) == "75%"
