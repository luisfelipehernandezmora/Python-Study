import requests
from pprint import pprint
i=0
params={
    "key":"3500ecce876792a90a078c86001b3cc7d5a78986",
    #"currency":"BTC"
}
url="https://api.nomics.com/v1/prices"
response=requests.get(url, params=params)
x=0
while response.json()[x]["currency"]!="BTC":
    x+=1
print(response.json()[x], x)



#pprint(response.json()[i])