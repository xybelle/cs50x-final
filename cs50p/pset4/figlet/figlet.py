import random
import sys

from pyfiglet import Figlet

figlet = Figlet()


fonts = figlet.getFonts()

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif sys.argv[1] != '--font' and sys.argv[1] != '-f':
        sys.exit("Invalid argument")
    elif sys.argv[2] not in fonts:
        sys.exit("Invalid font name")
    elif len(sys.argv) == 0:


    figlet.setFont(font=sys.argv[2])

    msg = input("Input: ")

    print(figlet.renderText(msg))


def random_font(msg):
    font = random.choice(fonts)
    figlet.setfont(font=font)
    print(figlet.renderText(msg))


def specific_font(msg, font):
    figlet.setfont(font=font)
    print(figlet.renderText(msg))
