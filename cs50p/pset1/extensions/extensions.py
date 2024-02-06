f = input("File name: ").lower()
i = "image/"
a = "application/"

if f.endswith('gif', 'jpg', 'jpeg', 'png'):
    i = f.index('.')
    print(f"image/{i}")

