import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if ums := re.findall(r"\bum\b", s):
        returm len(ums)


if __name__ == "__main__":
    main()
