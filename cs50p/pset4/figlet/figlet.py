import sys

from pyfiglet import Figlet

figlet = Figlet()


fonts = figlet.getFonts()

if len(sys.argv) > 2:
    sys.exit("Too many arguments")
if not sys.argv[1] == '--font' or not sys.argv[1] == '-f':
    sys.exit("Invalid argument")
elif sys.argv[2] not in fonts:
    sys.exit("Invalid font name")
