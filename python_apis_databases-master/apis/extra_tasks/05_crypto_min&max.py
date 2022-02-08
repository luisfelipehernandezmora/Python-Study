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
#Find the maximun and minimum 
import csv
import numpy as np
 
with open('Bitcoin price quest.csv', 'r') as f:
    data = list(csv.reader(f, delimiter=","))

data = np.array(data)
mini=0
maxi=0
values=[]
for x in data:
    value=float(x[1])
    values.append(value)
mini=min(values)
maxi=max(values)
min_time=""
max_time=""
for x in data: 
    if float(x[1])==mini:
        min_time=x[0]
    elif float(x[1])==maxi:
        max_time=x[0]
print(f"""The minimum price of BTC in this period was {mini} happend on {min_time} 
and the highest {maxi} that happend on {max_time}""")