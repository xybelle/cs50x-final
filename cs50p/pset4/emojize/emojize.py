import emoji

a = input("Input: ")
print(a)

for c in a:
    if ':' in c:
        print(emoji.emojize(f'{c}'))
    print(c, end="")

