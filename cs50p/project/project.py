import csv
from tabulate import tabulate

student_list = [
    {"stu_id": "1234", "name": "Harry"},
    {"stu_id": "4567", "name": "Ron"},
    {"stu_id": "7890", "name": "Hermione"},
]

gradebook = [
    {'name': 'Harry', 'Potions': '9', 'Charms': '9'},
    {'name': 'Hermione', 'Potions': '8', 'Charms': '10'},
    {'name': 'Ron', 'Potions': '7', 'Charms': '8'}
]

def main():
    main = [
        ["1", "Add Student"],
        ["2", "See Student List"],
        ["3", "Add Grade"],
        ["4", "See student gradebook"],
        ["5", "See all gradebook"],
        ["6", "Calculate Average"],
        #["7", "Generate Report"],
        ["8", "Exit"],
    ]

    while True:
        print("Main Menu")
        print(tabulate(main, headers=["Input", "Description"], tablefmt="fancy_outline"))
        selected = input("Select an option: ")
        if selected == "1":
            add_student()
        elif selected == "2":
            show_list()
        elif selected == "3":
            add_grade()
        elif selected == "4":
            show_stu_gradebook()
        elif selected == "5":
            show_gradebook()
        elif selected == "6":
            calculate_ave()
        elif selected == "7":
            generate_report()
        elif selected == "8":
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
    """Allows teacher to add a grade for a specific student and assignment/test."""
    while True:
        names = [_["name"] for _ in student_list]
        try:
            name = input("Student Name: ")
            if name not in names:
                print("\033[3mInvalid student name\033[0m")
                raise ValueError
            subj = input("Subject: ")
            grade = input("Grade: ")

            student_entry = next((entry for entry in gradebook if entry["name"] == name), None)
            if student_entry:
                student_entry[subj] = grade
                print("\033[3mGrade added successfully\033[0m")
            else:
                gradebook.append({"name": name, subj: grade})
                print("\033[3mGrade added successfully\033[0m")
            break
        except ValueError:
            pass


def show_stu_gradebook():
    """Allows teacher to view a student gradebook"""
    while True:
        names = [_["name"] for _ in student_list]
        try:
            name = input("Student Name: ")
            if name not in names:
                print("\033[3mInvalid student name\033[0m")
                raise ValueError
        except ValueError:
            pass

        stu_gradebook = filter(lambda s: s["name"] == name, gradebook)
        print(tabulate(stu_gradebook, headers="keys", tablefmt="fancy_outline"))
        back = input("Enter 1 to go back to main menu: ")
        if back == "1":
            break


def show_gradebook():
    """Allows teacher to view a student gradebook"""
    while True:
        print(tabulate(gradebook, headers="keys", tablefmt="fancy_outline"))
        back = input("Enter 1 to go back to main menu: ")
        if back == "1":
            break


def calculate_ave():
    """Calculates the average grade for a specific student"""
    while True:
        grades = []
        for student in gradebook:
            stu_grades = {}
            for subject, grade in student.items():
                if subject == "name":
                    continue
                stu_grades[subject] = int(grade)
            average_grade = sum(stu_grades.values()) / len(stu_grades) if stu_grades else 0
            grades.append({"name": student["name"], **stu_grades, "ave": average_grade})
        print(tabulate(grades, headers="keys", tablefmt="fancy_outline"))
        get_report = input("Generate report? (Y/N) ").toupper()
        if get_report == "Y":
            generate_report(grades)
        elif get_report == "N":
            break


def generate_report(grades):
    """Generate report of all grades for all student"""
    fieldnames = []
    for grade in grades:
        for key in grade.keys():
            if key not in fieldnames:
                fieldnames.append(key)
    with open("gradebook.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in grades:
            writer.writerow(row)

    print("\033[3mSuccessfully generated: gradebook.csv\033[0m")


if __name__ == "__main__":
    main()
