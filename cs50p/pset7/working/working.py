import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    valid_time = validate_input(s)
    if valid_time[1] == "PM":
        hour1 = for_pm(valid_time[0])
    if valid_time[4] == "PM":
        hour2 = for_pm(valid_time[0])
    return f"{}"


def validate_input(s):
    try:
        if matches := re.search(r"((?:1[0-2]|[1-9]):?[0-5]?[0-9]?) (AM|PM) to ((?:1[0-2]|[1-9]):?[0-5]?[0-9]?) (AM|PM)", s):
            return matches.groups()
        else:
            raise ValueError
    except ValueError:
        sys.exit("Hours: time AM/PM to time AM/PM")


def for_pm(time):
    if ":" in valid_time[0]:
            h, m = valid_time[0].split(":")
            h = int(h) + 12
            hh = f"{h}:{m}"
            return hh
    else:
        h = int(valid_time[0]) + 12
        return h

if __name__ == "__main__":
    main()

