vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def main():
    s = input("Input: ")
    print(shorten(s))


def shorten(word):
    for vowel in vowels:
        word = word.replace(f"{vowel}", "")
    return(word)


if __name__ == "__main__":
    main()
