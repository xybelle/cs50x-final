from tabulate import tabulate

student_list = []

def main():
    main = [["1", "Add Student"], ["2", "Add Grade"], ["3", "Calculate Average"],
            ["4", "Generate Report"]]
    selected = input(tabulate(main, headers=["Input", "Description"], tablefmt="fancy_outline"))


def add_student():
    """Allows teacher to add a student in db"""
    name = input("Student name: ")
    stu_id = input("Student ID: ")



def add_grade(student_id, test_id, grade):
    """
    Allows teacher to add a grade for a specific student and assignment/test.

    :param student_id, test_id, grade
    :type student_id: int, test_id: int, grade: float
    :raise ValueError: if student_id not in db
    """


def get_average(student_id):
    """
    Calculates the average grade for a specific student

    :param student_id: identifier
    :type student_id: int
    :raise ValueError: If student_id not in db
    :return: Grade average
    :rtype: float
    """


def generate_report(student_id):
    """
    Generate report of all grades for a specific student

    :param student_id
    :type student_id: int
    :raise ValueError: If student_id not in db
    :return: A csv file of grade
    """


if __name__ == "__main__":
    main()
