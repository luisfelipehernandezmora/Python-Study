# import requests
# from pprint import pprint
# i=0
# params={
#     "key":"3500ecce876792a90a078c86001b3cc7d5a78986",
# }
# url="https://api.nomics.com/v1/prices"
# response=requests.get(url, params=params)
# #Use this section to find the index of bitcoin in the API
# index=0
# while response.json()[index]["currency"]!="BTC":
#     index+=1

# print(response.json()[index], index) #This is to make sure we have what we want
# price=float(response.json()[index]["price"]) #Make it a float to manipulate it and round
# price=round(price,2) #this is what we want
# print(price) 

# import time

# start=time.time()
# local=time.localtime()
# time_string = time.strftime("%H:%M:%S")
# time_string2 = time.strftime("%c")
# timer=0
# while timer<14:
#     time_string = time.strftime("%H:%M:%S")
#     print(time_string, f"timer: {timer}")
#     timer+=2.5
#     time.sleep(3)
# import csv

# for n in range (10):
#     data = ["This", "is", "a", n]
#     with open('example.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow(data)

import time

ful_date=time.strftime("%c")
print(f"Today is {ful_date}")