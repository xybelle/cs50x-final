import random
import sys

from pyfiglet import Figlet

figlet = Figlet()


fonts = figlet.getFonts()

def main():
    msg = input("Input: ")
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv) == 1:
        random_font(msg)
    elif len(sys.argv) == 3:
        if sys.argv[1] != '--font' and sys.argv[1] != '-f':
            sys.exit("Invalid argument")
        elif sys.argv[2] not in fonts:
            sys.exit("Invalid font name")

        specific_font(msg, sys.argv[2])


def random_font(msg):
    font = random.choice(fonts)
    figlet.setFont(font=font)
    print("Output: ")
    print(figlet.renderText(msg))


def specific_font(msg, font):
    figlet.setFont(font=font)
    print("Output: ")
    print(figlet.renderText(msg))


main()
