from tabulate import tabulate

student_list = [
    {"id": "000001", "name": "Hermione"},
    {"id": "000002", "name": "Harry"},
    {"id": "000003", "name": "Ron"}
]

test_scores = []

def main():
    main = [["1", "See Student List"], ["2", "Add Grade"], ["3", "Calculate Average"],
            ["4", "Generate Report"]]
    selected = input(tabulate(main, headers=["Input", "Description"], tablefmt="fancy_outline"))
    match selected:
        case "1":
            show_list()


def show_list():
    """Allows teacher to view student list"""
    print(tabulate(student_list, headers="keys", tablefmt="fancy_outline"))


def add_grade(student_id, test_id, grade):
    """
    Allows teacher to add a grade for a specific student and assignment/test.

    :param student_id, test_id, grade
    :type student_id: str, test_id: str, grade: float
    :raise ValueError: if student_id not in db
    """


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
