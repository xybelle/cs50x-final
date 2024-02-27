from project import show_list

def test_show_list_empty(capfd, monkeypatch):
    # Mock input to simulate user pressing enter
    monkeypatch.setattr('builtins.input', lambda _: "")
    # Call function
    show_list()
    # Capture the output
    out, err = capfd.readouterr()
    # Assert that the output is as expected
    assert "\033[3mNo students added yet\033[0m\n" in out

def test_show_list_not_empty(capfd, monkeypatch):
    # Mock input to simulate user pressing enter
    monkeypatch.setattr('builtins.input', lambda _: "")
    # Call function
    show_list()
    out, err = capfd.readouterr()
    # Assert that the output is as expected
    assert 
