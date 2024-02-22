import inflect

p = inflect.engine()


from datetime import date


def main():
    dob = input("Date of Birth: ")
    age = p.number_to_words(dob)
    print(age.replace(' and', ''))


if __name__ == "__main__":
    main()
