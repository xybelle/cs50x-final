f = input("File name: ").lower().lstrip().rstrip().partition('.')

if f

if f[2] == 'gif' or f[2] == 'jpg' or f[2] == 'jpeg' or f[2] == 'png':
    if f[2] == 'jpg' or f[2] == 'jpeg':
        print("image/jpeg")
    print(f"image/{f[2]}")
elif f[2] == 'pdf' or f[2] == 'zip':
    print(f"application/{f[2]}")
elif f[2] == 'txt':
    print("text/plain")
else:
    print("application/octet-stream")
