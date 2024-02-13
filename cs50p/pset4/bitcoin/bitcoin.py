import json
import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Usage: python bitcoin.py n")
elif not sys.argv[1].isdigit():
    sys.exit("n is not an integer")

n = float(sys.argv[1])

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit()

#p = {"bpi":{"USD":{"rate"}}}
#r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json", params=p)
res = response.json()
#price = bpi USD rate
#current_cost = n *


print(res)
