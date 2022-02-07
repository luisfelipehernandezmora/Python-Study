'''
http://docs.nomics.com/
Using the nomics API, repeatedly fetch the price of Bitcoin for a duration of 10 minutes.
Store each value in a dictionary that uses the time of query as a key.

After the script stopped running, determine programmatically at what query time the price
was the highest, and when the lowest.

HINTS:
- request an API key first and remember to include it in your queries
- the /prices endpoint of the nomics API can be used for achieving this task
- remember to use packages from the standard library, e.g. for time keeping and dates

BONUS: Explore the logging package for easier tracking

'''
import requests
from pprint import pprint
# url="https://api.nomics.com/v1/currencies/ticker?key=3500ecce876792a90a078c86001b3cc7d5a78986&ids=BTC,ETH,XRP&interval=1d,30d&convert=EUR&platform-currency=ETH&per-page=100&page=1"
# request=requests.get(url).json()["price"]
# pprint(request)


# import urllib.request
# url = """https://api.nomics.com/v1/currencies/ticker?
# key=your-key-here
# &ids=BTC,ETH,XRP
# &interval=1d,30d
# &convert=EUR
# &platform-currency=ETH
# &per-page=100
# &page=1"""
# print(urllib.request.urlopen(url).read())

params={
    "key":"3500ecce876792a90a078c86001b3cc7d5a78986",
    "ids": "BTC,ETH", #"BTC,ETH,XRP
    "interval":"1d,30d",
    "convert":"EUR",
    "platform-currency":"ETH",
    "per-page":100,
    "page":1,
}
url="https://api.nomics.com/v1/currencies/ticker"
response=requests.get(url, params=params)
pprint(response.json()[0]["price"])
#a=response.json()
print(response.status_code)
