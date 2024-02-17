import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = re.search(r".+src=\"https://www\.youtube\.com/embed/(\w+)\".+", s)
    vid_id = url.groups(1)
    print(vid_id)
    return vid_id.strip("(", ")", "")

...


if __name__ == "__main__":
    main()
