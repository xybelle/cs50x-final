import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = re.search(r".+src=\"https://www\.youtube\.com/embed/(\w+)\".+", s)
    print(url)

...


if __name__ == "__main__":
    main()
