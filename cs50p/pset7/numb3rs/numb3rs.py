import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    n = ip.strip(".")
    if max_255(n):
        if valid := re.search(r"[0-2]?[0-9]?[0-9]?\.{3}[0-2]?[0-9]?[0-9]?", ip):
            print("True")
    else:
        print("False")


def max_255(num):
    parts = num.split(".")
    for part in parts:
        if int(part) > 255:
            return False
    return True


if __name__ == "__main__":
    main()
