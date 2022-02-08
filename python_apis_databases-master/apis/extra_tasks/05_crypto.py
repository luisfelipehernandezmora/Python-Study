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
import time
import csv
ful_date=time.strftime("%c")
print(f"Today is {ful_date}")

timer=0
increment=1
btc_history={}
while timer<600:
    time_string = time.strftime("%H:%M:%S")
    params={
        "key":"3500ecce876792a90a078c86001b3cc7d5a78986",
    }
    url="https://api.nomics.com/v1/prices"
    response=requests.get(url, params=params)
    index=0 #Use this section to find the index of bitcoin in the API of nomics
    while response.json()[index]["currency"]!="BTC":
        index+=1   
    print(response.json()[index], index, time_string)
    
    price=(response.json()[index]["price"])
    #price=round(price,2)
    btc_history[time_string]=price
    timer+=22
    time.sleep(increment)
btc_history
for key in btc_history.keys():
    with open ("Bitcoin price exercise.txt","a") as file:
        file.write(f"Time: {key}  the price of Bitcoin was: {btc_history[key]} USD \n")
    print("Date : {} , Price in USD : {}".format(key,btc_history[key]))

for key in btc_history.keys():
    #data = ["Date searched ",key," ","Price in USD ",btc_history[key]]
    data = [key,btc_history[key]]
    with open('Bitcoin price quest.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)
