'''
Sign up for an API key with the coinmarketcap API.
#url="https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=07578228-789a-48dd-966a-2b845a995b2d&start=1&limit=100&convert=USD"

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
import csv
limit=1000
params={
    "CMC_PRO_API_KEY":"07578228-789a-48dd-966a-2b845a995b2d",
    "start":"1",
    "limit":str(limit),
    "convert":"USD",
}
url="https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

response=requests.get(url, params=params)
for x in range (0,limit):
    name=response.json()["data"][x]["name"]
    symbol=response.json()["data"][x]["symbol"]
    price=response.json()["data"][x]["quote"]["USD"]["price"]
    rank=response.json()["data"][x]["cmc_rank"]
    platform=response.json()["data"][x]["platform"]
    print(f"The {name} ({symbol}) have a price of {price} USD, has the cmc rank of {rank} and {platform} platform")
    data=[name, symbol, price, rank, platform]
    with open ("Crytocurrencies_information.txt","a") as file:
        file.write(f"The {name} ({symbol}) have a price of {price} USD, has the cmc rank of {rank} and {platform}  \n")
    with open('Crytocurrencies_information.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)

