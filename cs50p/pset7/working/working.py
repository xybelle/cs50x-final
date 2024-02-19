import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    valid_time = validate_input(s)
    if first := re.search(r"(?:1[0-2]|[1-9]):[0-5][0-9]", valid_time[0]):
        h1, m1 = valid_time[0].split(":")
        if h1 == "12":
            h1 = 0
        else:
            h1 = int(h1) + 12
    elif first := re.search(r"(?:1[0-2]|[1-9])", valid_time[0]):
        h1 = int(valid_time[0])
        m1 = 0

    if second := re.search(r"(?:1[0-2]|[1-9]):[0-5][0-9]", valid_time[2]):
        h2, m2 = valid_time[2].split(":")
        if h2 == "12":
            h2 = 0
        else:
            h2 = int(h2) + 12
    elif second := re.search(r"(?:1[0-2]|[1-9])", valid_time[2]):
        h2 = int(valid_time[2])
        m2 = 0

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


def validate_input(s):
    try:
        if matches := re.search(r"((?:1[0-2]|[1-9]):?([0-5][0-9])?) (AM|PM) to ((?:1[0-2]|[1-9]):?([0-5][0-9])?) (AM|PM)", s):
            return matches.groups()
        else:
            raise ValueError
    except ValueError:
        sys.exit("Hours: time AM/PM to time AM/PM")


if __name__ == "__main__":
    main()




