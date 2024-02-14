vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#s = input("Input: ")

#for c in s:
#    if c in vowels:
#        continue
#    print(c, end="")
#print()


def main():
    s = input("Input: ")
    print(shorten(s))


def shorten(word):
    for c in word:
        if c in vowels:
            continue
    return(c)


if __name__ == "__main__":
    main()
