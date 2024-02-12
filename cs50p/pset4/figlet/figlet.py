import random
import sys

from pyfiglet import Figlet

figlet = Figlet()


fonts = figlet.getFonts()

def main():
    msg = input("Input: ")
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif sys.argv[1] != '--font' and sys.argv[1] != '-f':
        sys.exit("Invalid argument")
    elif sys.argv[2] not in fonts:
        sys.exit("Invalid font name")
    else:
        print_message(msg, sys.argv[2])


def print_message(msg, font=None):
    if font is None:
        font = random.choice(fonts)
    figlet.setFont(font=font)
    print("Output: ")
    print(figlet.renderText(msg))


main()
