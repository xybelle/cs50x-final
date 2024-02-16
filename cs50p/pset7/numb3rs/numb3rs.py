import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    re.search(r"(0-2)?(0-5)?(0-5)?\.")



...


if __name__ == "__main__":
    main()
