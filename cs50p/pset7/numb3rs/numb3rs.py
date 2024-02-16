import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    sets = ip.split(".")
    if not sets.isdigit():
        return False
    if valid := re.search(r"([0-2]?[0-9]?[0-9]?\.){3}[0-2]?[0-9]?[0-9]?", ip):
        if max_255(ip) and four_sets(ip):
            return True
    return False


def max_255(digits):
    digits = digits.split(".")
    for digit in digits:
        if int(digit) > 255:
            return False
            break
    return True


def four_sets():
    if len(sets) > 4:
        return False
    return True


if __name__ == "__main__":
    main()
