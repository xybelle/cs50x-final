f = input("File name: ").lower()
i = "image/"
a = "application/"

if f.endswith('gif') or f.endswith('jpg') or f.endswith('jpeg') or f.endswith('png'):
    i = f.partition('.')
    print(i)
    print(f"image/{i[2]}")

