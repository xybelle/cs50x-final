def main():
    print(tabulate)


def add_student():
    """Allows teacher to add a student in db"""


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
