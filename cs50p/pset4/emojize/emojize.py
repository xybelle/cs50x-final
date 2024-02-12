import emoji

a = {input("Input: ")}

for _ in a:
    if ':' in _:
        print(emoji.emojize('_'))
    print(_)

