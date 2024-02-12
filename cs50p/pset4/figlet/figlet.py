import sys

from pyfiglet import Figlet

figlet = Figlet()

a = figlet.getFonts()

print(a)

if len(sys.argv) > 2:
    sys.exit("Too many arguments")
if
