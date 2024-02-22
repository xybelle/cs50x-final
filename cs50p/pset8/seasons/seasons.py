import inflect

p = inflect.engine()


from datetime import date


def main():
    dob = date.fromisoformat(input("Date of Birth: "))
    print(get_age(dob))


def get_age(dob):
    age = date.today() - dob
    return age


#def sing(age):
#    s = p.number_to_words(dob)
#    return s.replace("and ", "")


if __name__ == "__main__":
    main()
