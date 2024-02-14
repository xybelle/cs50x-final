def main():
    greeting = input("Greeting: ").strip().lower()
    print(f"${value(greeting)}")
    sys.exit(0)


def value(greeting):
    if "hello" in greeting:
        return 0
    elif greeting[0] == 'h':
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
