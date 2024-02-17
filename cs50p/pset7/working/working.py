import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    valid_time = validate_input(s)


def validate_input(s):
    try:
        if matches := re.search(r"(\d:?\d?\d?) ([A|P|]M) to (\d:?\d?\d?) ([A|P|]M)", s):
            print(matches.groups())
        else:
            raise ValueError
    except ValueError:
        sys.exit("Hours: time AM/PM to time AM/PM")


if __name__ == "__main__":
    main()

