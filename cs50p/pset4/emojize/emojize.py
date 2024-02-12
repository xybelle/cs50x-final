import emoji

a = input("Input: ")
print("Output: ", end="")

for c in a:
    print(c, end="")
    if c == ':':
        break
print(emoji.emojize(f"{a}", language='alias'))

