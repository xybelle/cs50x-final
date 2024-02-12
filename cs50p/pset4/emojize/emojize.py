import emoji

a = input("Input: ")
print(a)

for c in a:
    print(c, end="")
print(emoji.emojize(f"{a}"))

