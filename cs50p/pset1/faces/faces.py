def main():
    message = input("Message: ")
    converted_message = convert(message)

    print(converted_message)

def convert(m):
    new_m = m.replace(":)", "🙂")
    return new_m

main()
