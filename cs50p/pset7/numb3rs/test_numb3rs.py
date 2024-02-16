from numb3rs import validate

def test_validate():
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True
    assert validate("275.1.1.1") == False
