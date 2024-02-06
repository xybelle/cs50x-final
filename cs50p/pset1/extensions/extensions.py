f = input("File name: ").lower().lstrip().rstrip().split('.')

if f.count('.') >= 2 or f.count('.') == 0:
    print("application/octet-stream")


if f[2] == 'gif' or f[2] == 'png':
    print(f"image/{f[2]}")
elif f[2] == 'jpg' or f[2] == 'jpeg':
    print("image/jpeg")
elif f[2] == 'pdf' or f[2] == 'zip':
    print(f"application/{f[2]}")
elif f[2] == 'txt':
    print("text/plain")
else:
    print("application/octet-stream")
