import json
import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Usage: python bitcoin.py n")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("n is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Error: Unable to retrieve data from CoinDesk API.")

res = response.json()

try:
    price = res["bpi"]["USD"]["rate"].replace(",", "")
except KeyError:
    sys.exit("Error)

current_cost = n * float(price)

print(f"${current_cost:,.4f}")
