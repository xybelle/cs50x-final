def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    if "hello" in greeting.lower():
        return 0
    elif greeting[0] == 'h' or greeting[0] == 'H':
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
