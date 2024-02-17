import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if found := re.search(r".+src=\"https?://(?:www\.)?youtube\.com/embed/(.+)\">? title.+?", s):
        print(found.group(1))
        return f"https://youtu.be/" + found.group(1)

...


if __name__ == "__main__":
    main()
