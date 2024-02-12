import sys

from pyfiglet import Figlet

figlet = Figlet()


fonts = figlet.getFonts()

if len(sys.argv) > 3:
    sys.exit("Too many arguments")
elif sys.argv[1] != '--font' or sys.argv[1] != '-f':
    sys.exit("Invalid argument")
elif sys.argv[2] not in fonts:
    sys.exit("Invalid font name")

figlet.setFont(font=sys.argv[2])

msg = input("Input: ")

print(figlet.renderText(msg))
