import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = re.search(r".+src=(.+).+", s)
    print(url)

...


if __name__ == "__main__":
    main()
