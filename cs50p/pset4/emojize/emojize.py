import emoji

a = input("Input: ")
print(a)

word = {}
i = 0
for c in a:
    word[i] = c
    if c == ' ':
        i += 1
        continue
print(word)
for _ in a:
    if ':' in _:
        print(emoji.emojize('_'))
    print(_)

