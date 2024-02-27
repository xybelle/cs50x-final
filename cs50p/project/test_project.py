import csv
import pytest
from unittest.mock import patch, call
from io import StringIO
from project import (add_student, add_grade, generate_report,
                         show_list, show_stu_gradebook, show_gradebook,
                         calculate_ave)

@pytest.fixture
def mock_input(monkeypatch):
    user_inputs = []

    def mock_input_impl(prompt):
        user_input = user_inputs.pop(0)
        print(prompt + user_input)
        return user_input

    monkeypatch.setattr('builtins.input', mock_input_impl)
    return user_inputs

def test_add_student(mock_input, capsys):
    # Simulate user input
    mock_input.extend(["Harry", "1234"])

    # Call the function
    add_student()

    # Check if the student was added
    assert {"stu_id": "1234", "name": "Harry"} in student_list

    # Check the printed message
    captured = capsys.readouterr()
    assert "Student successfully added" in captured.out

# Similar tests for other functions...

def test_generate_report(tmp_path, capsys):
    # Simulate gradebook data
    gradebook = [
        {'name': 'Harry', 'Potions': '9', 'Charms': '9'},
        {'name': 'Hermione', 'Potions': '8', 'Charms': '10'},
        {'name': 'Ron', 'Potions': '7', 'Charms': '8'}
    ]

    # Call the function
    generate_report()

    # Check if the CSV file was generated
    csv_file = tmp_path / "gradebook.csv"
    assert csv_file.exists()

    # Check the printed message
    captured = capsys.readouterr()
    assert "Successfully generated: gradebook.csv" in captured.out


