import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    valid_time = validate_input(s)
    if valid_time[1] == "PM":
        hour1 = for_pm(valid_time[0])
    elif valid_time[1] == "AM":
        hour1 = valid_time[0]
    if valid_time[3] == "PM":
        hour2 = for_pm(valid_time[2])
    elif valid_time[3] == "PM":
        hour2 = valid_time[2]

    return f"{hour1:02} to {hour2:02}"


def validate_input(s):
    try:
        if matches := re.search(r"((?:1[0-2]|[1-9]):?[0-5]?[0-9]?) (AM|PM) to ((?:1[0-2]|[1-9]):?[0-5]?[0-9]?) (AM|PM)", s):
            return matches.groups()
        else:
            raise ValueError
    except ValueError:
        sys.exit("Hours: time AM/PM to time AM/PM")


def for_pm(time):
    if ":" in time:
            h, m = time.split(":")
            h = int(h) + 12
            return f"{h}:{m}"
    else:
        h = int(time) + 12
        return f"{h}:00"

if __name__ == "__main__":
    main()

