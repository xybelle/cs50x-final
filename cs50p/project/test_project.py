import csv
import pytest
from unittest.mock import patch, call
from io import StringIO
from project import (add_student, add_grade, generate_report,
                         show_list, show_stu_gradebook, show_gradebook,
                         calculate_ave)

# Define student list for testing
student_list = [
    {"stu_id": "1234", "name": "Harry"},
    {"stu_id": "4567", "name": "Ron"},
    {"stu_id": "7890", "name": "Hermione"},
]

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

def test_show_stu_gradebook(mock_input, capsys):
    # Simulate gradebook data
    gradebook = [
        {'name': 'Harry', 'Potions': '9', 'Charms': '9'},
        {'name': 'Hermione', 'Potions': '8', 'Charms': '10'},
        {'name': 'Ron', 'Potions': '7', 'Charms': '8'}
    ]

    # Simulate user input
    mock_input.append("Harry")

    # Call the function
    show_stu_gradebook()

    # Check if the correct student gradebook is shown
    captured = capsys.readouterr()
    assert "Harry" in captured.out
    assert "Potions" in captured.out
    assert "9" in captured.out
    assert "Charms" in captured.out
    assert "9" in captured.out

    # Check if the prompt to go back to the main menu is shown
    assert "Enter 1 to go back to main menu: " in captured.out
