import emoji

a = input("Input: ")
print(a)
print("Output: ", end="")
print(emoji.emojize(f"{a}", language='alias'))

