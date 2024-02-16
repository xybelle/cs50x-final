import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    n = ip.strip(".")
    if max_255(n):
        if valid := re.search(r"[0-2]?[0-9]?[0-9]?\.{3}[0-2]?[0-9]?[0-9]?"):
            print("True")
    else:
        print("False")


def max_255(num):
    m = num.split(".")
    for _ in m:
        if int(m[_]) > 255:
            return False
    return True


if __name__ == "__main__":
    main()
