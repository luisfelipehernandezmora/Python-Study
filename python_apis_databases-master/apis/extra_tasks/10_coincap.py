'''
Sign up for an API key with the coinmarketcap API.

Using their documentation, fetch all listed cryptocurrencies.
From the result, create a new JSON file that includes the following:
* cmc_rank
* name
* symbol
* platform
* quote
Save that info to a file.
'''
import requests
from pprint import pprint

#url="https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=07578228-789a-48dd-966a-2b845a995b2d&start=1&limit=100&convert=USD"
url="https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

response=requests.get(url)
params={
    "CMC_PRO_API_KEY":"07578228-789a-48dd-966a-2b845a995b2d",
    "start":"1",
    "limit":"100",
    "convert":"USD",
}