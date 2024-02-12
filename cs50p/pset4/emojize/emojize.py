import emoji

a = input("Input: ")
print(a)

for _ in a:
    if ':' in _:
        print(emoji.emojize('_'))
    print(_)

