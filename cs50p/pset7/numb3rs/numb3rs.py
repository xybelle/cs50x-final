import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    n = ip.strip(".")
    if max_255(n):
        re.search(r"[0-2]?[0-9]?[0-9]?\.")


def max_255(num):
    for _ in num:
        if int(num) > 255:
            return False
    return True


if __name__ == "__main__":
    main()
