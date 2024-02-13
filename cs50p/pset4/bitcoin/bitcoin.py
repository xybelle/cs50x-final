import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Usage: python bitcoin.py n")
elif not sys.argv[2].isdigit():
    sys.exit("n is not an integer")

n = float(sys.argv[2])
