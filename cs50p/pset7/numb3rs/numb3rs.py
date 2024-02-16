import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if valid := re.search(r"[0-2]?[0-9]?[0-9]?\.{3}[0-2]?[0-9]?[0-9]?", ip):
        numbers = ip.split(".")
        if max_255(numbers) == True:
            print("True")
        else:
            print("False")


def max_255(parts):
    for part in parts:
        if int(part) > 255:
            return False
            break
    return True


if __name__ == "__main__":
    main()
