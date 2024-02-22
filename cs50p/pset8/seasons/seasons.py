import inflect

p = inflect.engine()


from datetime import date


def main():
    dob = input("Date of Birth: ")
    print(p.number_to_words(dob))


if __name__ == "__main__":
    main()
