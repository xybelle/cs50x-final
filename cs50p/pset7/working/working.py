import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    valid_time = validate_input(s)
    if ":" in valid_time[0]:
        h, m = valid_time[0].split(":")
    if ":" in valid_time[2]:
        h, m = valid_time[2].split(":")
        hh = int(h) + 12


def validate_input(s):
    try:
        if matches := re.search(r"((?:1[0-2]|[1-9]):?[0-5]?[0-9]?) (AM|PM) to ((?:1[0-2]|[1-9]):?[0-5]?[0-9]?) (AM|PM)", s):
            return matches.groups()
        else:
            raise ValueError
    except ValueError:
        sys.exit("Hours: time AM/PM to time AM/PM")


if __name__ == "__main__":
    main()

