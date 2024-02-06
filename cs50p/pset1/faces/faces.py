def convert(m):
    new_m = m.replace(":)", "🙂")
    return new_m

def main():
    message = input("How are you? ")
    converted_message = convert(message)

    print(converted_message)

main()
