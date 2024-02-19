import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if ums := re.findall(r".+?[]", s):
        return len(ums.groups)


...


if __name__ == "__main__":
    main()
