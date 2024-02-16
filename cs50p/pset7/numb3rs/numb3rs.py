import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    sets = ip.split(".")

    if valid := re.search(r"([0-2]?[0-9]?[0-9]?\.){3}[0-2]?[0-9]?[0-9]?", ip):
        if max_255(sets) and four_sets(sets):
            return True
    return False


def max_255(digits):
    for digit in digits:
        if int(digit) > 255:
            return False
            break
    return True


def four_sets(n):
    if not n.isdigit():
        return False
    if len(n) > 4:
        return False
    return True


if __name__ == "__main__":
    main()
