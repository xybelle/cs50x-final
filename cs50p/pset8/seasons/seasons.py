import inflect

p = inflect.engine()


from datetime import date


def main():
    dob = date.fromisoformat(input("Date of Birth: "))
    print(f"{sing(get_age(dob))} minutes")


def get_age(dob):
    age = date.today() - dob
    return age.days * 24 * 60


def sing(age):
    s = p.number_to_words(age)
    return s.replace("and ", "")


if __name__ == "__main__":
    main()
