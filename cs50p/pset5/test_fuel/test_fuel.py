from fuel import convert, gauge


def test_convert():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("4/3") == ValueError
    assert convert("2/0") == ZeroDivisionError

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(75) == "75%"
