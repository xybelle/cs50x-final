import inflect

p = inflect.engine()


from datetime import date


def main():
    dob = date.fromisoformat(input("Date of Birth: "))
    age = sing(dob)


def sing(dob):
    s = p.number_to_words(dob)
    return s.replace("and ", "")


def get_age(dob):
    age = date.today() - dob



if __name__ == "__main__":
    main()
