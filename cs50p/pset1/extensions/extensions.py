f = input("File name: ").lower().partition('.')

if f.endswith('gif') or f.endswith('jpg') or f.endswith('jpeg') or f.endswith('png'):
    print(f"image/{f[2]}")
elif f.endswith('pdf') or f.endswith('zip'):
    print(f"application/{f[2]}")
elif f.endswith('txt'):
    print(f"txt/{f[2]}")

