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

def test_generate_report(capsys):
    # Call the function
    generate_report()

    # Check if the expected message is printed
    captured = capsys.readouterr()
    assert "Successfully generated: gradebook.csv" in captured.out

    # Check if the CSV file is generated
    with open("gradebook.csv", "r") as csvfile:
        # Read the contents of the CSV file
        csv_content = csvfile.read()

    # Check if the CSV file contains the expected headers
    assert "name,Potions,Charms,ave\n" in csv_content

    # Check if the CSV file contains the expected data
    assert "Harry,9,9,9.0\n" in csv_content
    assert "Hermione,8,10,9.0\n" in csv_content
    assert "Ron,7,8,7.5\n" in csv_content


def test_show_stu_gradebook():
    # Mocking input to provide a student name
    with patch('builtins.input', side_effect=['Harry']):
        # Call the function that needs to be tested
        show_stu_gradebook()

