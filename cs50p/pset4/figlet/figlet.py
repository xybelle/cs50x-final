import sys

from pyfiglet import Figlet

figlet = Figlet()


fonts = figlet.getFonts()
f = sys.argv[1]
print(f)
if len(sys.argv) > 3:
    sys.exit("Too many arguments")
elif f != '--font' or f != '-f':
    sys.exit("Invalid argument")
elif sys.argv[2] not in fonts:
    sys.exit("Invalid font name")

figlet.setFont(font=sys.argv[2])

msg = input("Input: ")

print(figlet.renderText(msg))
