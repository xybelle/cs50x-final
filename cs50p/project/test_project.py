import project


def test_show_list_empty(capfd, monkeypatch):
    # Mock input to simulate user pressing enter
    monkeypatch.setattr("builtins.input", lambda _: "")
    # Mock student_list to be an empty list
    monkeypatch.setattr("project.student_list", [])
    # Call function
    project.show_list()
    # Capture the output
    out, err = capfd.readouterr()
    # Assert that the output is as expected
    assert "\033[3mNo students added yet\033[0m\n" in out

def test_show_list_not_empty(capfd, monkeypatch):
    # Mock input to simulate user pressing enter
    monkeypatch.setattr('builtins.input', lambda _: "")
    # Mock student_list to have an entry
    monkeypatch.setattr("project.student_list", [{"stu_id": "1234", "name": "Harry"}])
    # Call function
    project.show_list()
    out, err = capfd.readouterr()
    # Assert that the output is as expected
    assert "1234" in out
    assert "Harry" in out

def test_add_student_new(capfd, monkeypatch):
    # Mock input to simulate user entering a name and ID
    inputs = iter(["Gabbie", "3456"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    # Mock student_list to be an empty list
    monkeypatch.setattr("project.student_list", [])
    # Call function
    project.add_student()
    # Capture the output
    out, err = capfd.readouterr()
    # Assert that the output is as expected
    assert "\033[3mStudent successfully added\033[0m\n" in out

def test_add_student_none(capfd, monkeypatch):
    # Mock input to simulate user not entering name and id
    inputs = iter(["", "", "Gabbie", "3456"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    # Mock student_list to be an empty list
    monkeypatch.setattr("project.student_list", [])
    # Call function
    project.add_student()
    # Capture the output
    out, err = capfd.readouterr()
    # Assert that the output is as expected
    assert "Please enter name/id" in out
    assert "\033[3mStudent successfully added\033[0m\n" in out

def test_add_student_not_new(capfd, monkeypatch):
    # Mock input to simuate user entering and id that's already in student_list
    inputs = iter(["Gabbie", "1234", "Gabbie", "3456"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    # Mock student list
    monkeypatch.setattr("project.student_list", [{"stu_id": "1234", "name": "Harry"}])
    # Call function
    project.add_student()
    # Capture the output
    out, err = capfd.readouterr()
    # Assert that the output is as expected
    assert "Student ID already in use" in out
    assert "\033[3mStudent successfully added\033[0m\n" in out
