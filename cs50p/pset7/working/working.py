import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := (re.search(r"\d:?\d?\d? [A|P|M] to \d:?\d?\d?"))


...


if __name__ == "__main__":
    main()

