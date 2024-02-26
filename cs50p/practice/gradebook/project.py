from cs50 import SQL
from tabulate import tabulate

student_list = [
    {"stu_id": "1234", "name": "Harry"},
    {"stu_id": "4567", "name": "Ron"}
]

gradebook = []

def main():
    main = [
        ["1", "Add Student"],
        ["2", "See Student List"],
        ["3", "Add Grade"],
        ["4", "See gradebook"],
        ["5", "Calculate Average"],
        ["6", "Generate Report"],
        ["7", "Exit"],
    ]

    while True:
        print(tabulate(main, headers=["Input", "Description"], tablefmt="fancy_outline"))
        selected = input("Select an option: ")
        if selected == "1":
            add_student()
        elif selected == "2":
            show_list()
        elif selected == "3":
            add_grade()
        elif selected == "4":
            show_gradebook()
        elif selected == "6":
            print("Exiting...")
            break
        else:
            print("Invalid Input. Please select a valid option.")


def show_list():
    """Allows teacher to view student list"""
    while True:
        print(tabulate(student_list, headers="keys", tablefmt="fancy_outline"))
        back = input("Enter 1 to go back to main menu: ")
        if back == "1":
            break


def add_student():
    """Allows teacher to add student to student list"""
    while True:
        name = input("Student name: ")
        id = input("Student ID: ")
        try:
            student_list.append({"stu_id": id, "name": name})
            print("\033[3mStudent successfully added\033[0m")
            break
        except ValueError:
            pass


def add_grade():
    """
    Allows teacher to add a grade for a specific student and assignment/test.

    :param student_id, test_id, grade
    :type student_id: str, test_id: str, grade: float
    :raise ValueError: if student_id not in db
    """

    while True:
        names = [_["name"] for _ in student_list]
        try:
            name = input("Student Name: ")
            if name not in names:
                print("Invalid student name")
                raise ValueError
            subj = input("Subject: ")
            grade = input("Grade: ")
            gradebook.append({subj: grade})
            break
        except ValueError:
            pass


def show_gradebook():
    """Allows teacher to view student list"""
    while True:
        print(tabulate(gradebook, headers="keys", tablefmt="fancy_outline"))
        back = input("Enter 1 to go back to main menu: ")
        if back == "1":
            break


def get_average(student_id):
    """
    Calculates the average grade for a specific student

    :param student_id: identifier
    :type student_id: str
    :raise ValueError: If student_id not in db
    :return: Grade average
    :rtype: float
    """


def generate_report(student_id):
    """
    Generate report of all grades for a specific student

    :param student_id
    :type student_id: str
    :raise ValueError: If student_id not in db
    :return: A csv file of grade
    """


if __name__ == "__main__":
    main()
