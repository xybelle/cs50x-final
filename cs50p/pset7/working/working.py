import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    valid_time = validate_input(s)
    if first := re.search(r"(?:1[0-2]|[1-9]):[0-5][0-9]", valid_time[0]):
        h1, m1 = hours_mins_fmt(valid_time[0], valid_time[1])
    elif first := re.search(r"(?:1[0-2]|[1-9])", valid_time[0]):
        h1, m1 = hours_fmt(valid_time[0], valid_time[1])

    if second := re.search(r"(?:1[0-2]|[1-9]):[0-5][0-9]", valid_time[2]):
        h2, m2 = hours_mins_fmt(valid_time[2], valid_time[3])

    elif second := re.search(r"(?:1[0-2]|[1-9])", valid_time[2]):
        h2, m2 = hours_fmt(valid_time[2], valid_time[3])

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


def validate_input(s):
    try:
        if matches := re.search(r"((?:1[0-2]|[1-9]):?([0-5][0-9])?) (AM|PM) to ((?:1[0-2]|[1-9]):?([0-5][0-9])?) (AM|PM)", s):
            return matches.groups()
        else:
            raise ValueError
    except ValueError:
        sys.exit()


def hours_mins_fmt(time, midday):
    h, m = time.split(":")
    if midday == "AM":
        if  h == "12":
            h = 0
        return h, m
    if midday == "PM":
        h = int(h) + 12
        return h, m


def hours_fmt(time, midday):
    h = time
    m = 0
    if midday == "AM":
        if h == "12":
            h = 0
        return h, m
    if midday == "PM":
        h = int(h) + 12
        return h, m


if __name__ == "__main__":
    main()
