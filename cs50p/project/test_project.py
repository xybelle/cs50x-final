from project import show_list

# Mock empty student list for testing
student_list_empty = []

# Mock student list for testing
student_list = [
    {"stu_id": "1234", "name": "Harry"},
    {"stu_id": "4567", "name": "Ron"},
    {"stu_id": "7890", "name": "Hermione"},
]
def test_show_list_empty(capfd, monkeypatch):
    # Mock input to simulate user pressing enter
    monkeypatch.setattr('builtins.input', lambda _: "")
    monkeypatch.delitem(project.student_list, "stu_id", "name" raising=False)
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
    assert "Press enter to go back to main menu\n" in out
