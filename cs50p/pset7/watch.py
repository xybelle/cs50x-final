import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if found := re.search(r".+src=\"https://www\.youtube\.com/embed/(.+)\">? title.+", s):
        return found.groups(1)
    print(found.groups(1))

...


if __name__ == "__main__":
    main()
