import requests
import sys
import json
try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    if not type(sys.argv[1]) != float:
        sys.exit("Command-line argument is not a number")

    n = float(sys.argv[1])

    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    # print(json.dumps(r.json(), indent = 1))

    r = r.json()
    o = float(r["bpi"]["USD"]["rate_float"])
    print(f"${o*n:,.4f}")
except requests.RequestException:
    pass