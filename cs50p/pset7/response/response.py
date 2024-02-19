from validator_collection import checkers, errors


def main():
    print(validate(input("What's your email address?")))


def validate(email):
    return checker.is_email(email)


if __name__ == "__main__":
    main()
