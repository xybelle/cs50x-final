import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if found := re.search(r".+src=\"https://www\.youtube\.com/embed/(\w+)\".+", s):
        return found.groups(1)
    print(vid_id)

...


if __name__ == "__main__":
    main()
