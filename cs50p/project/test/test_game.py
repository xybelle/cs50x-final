
from main_code import addition_quiz

def test_addition_quiz(monkeypatch):
    # Simulate user input
    user_input = ['5', '7', '12']  # Inputs to simulate for x + y = 12
    def mock_input(_):
        return user_input.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)

    # Call the function
    correct_answers = addition_quiz()

    # Assert that the correct answers are counted
    assert correct_answers == 1
