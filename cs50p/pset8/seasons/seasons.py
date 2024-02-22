import inflect

p = inflect.engine()


from datetime import date


def main():
    print(f"{sing(get_age(get_dob))} minutes")


def get_dob():
    dob = date.fromisoformat(input("Date of Birth: "))
    return dob


def get_age(dob):
    age = date.today() - dob
    return age.days * 24 * 60


def sing(age):
    s = p.number_to_words(age)
    return s.replace("and ", "")


if __name__ == "__main__":
    main()
