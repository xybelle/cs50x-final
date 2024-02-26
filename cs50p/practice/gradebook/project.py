from tabulate import tabulate

#student_list = [
#    {"id": "000001", "name": "Hermione"},
#    {"id": "000002", "name": "Harry"},
#    {"id": "000003", "name": "Ron"}
#]

test_scores = [
    {"stu_id": "", "name": "", "1st": "", "2nd": "", "3rd": "", "4th": "", "Ave": ""}
]

def main():
    main = [
        ["1", "Add Student"],
        ["2", "See Student List"],
        ["3", "Add Grade"],
        ["4", "Calculate Average"],
        ["5", "Generate Report"],
        ["6", "Exit"]
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
        elif selected == "6":
            print("Exiting...")
            break
        else:
            print("Invalid Input. Please select a valid option.")


def show_list():
    """Allows teacher to view student list"""
    while True:
        print(tabulate(test_scores, headers="keys", tablefmt="fancy_outline"))
        back = input("Enter 1 to go back to main menu: ")
        if back == "1":
            break


def add_student():
    """Allows teacher to add student to student list"""
    while True:
        name = input("Student name: ")
        id = input("Student ID: ")
        try:
            test_scores.append({"stu_id": id, "name": name})
            print("Successfully added student")
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

    student_list = [{"id": test_scores[_], "name": test_scores[_]} for _ in test_scores]
    while True:
        print(student_list)
        print("Select Student: ")
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
