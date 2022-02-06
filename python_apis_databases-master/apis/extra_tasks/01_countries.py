'''
Use the countries API https://restcountries.com/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals
'''
import requests
from pprint import pprint

url="https://restcountries.com/v3.1"

country1=input("Which country you want to know about? ")
country2=input("Which other country you want to know about? ")

name1=requests.get(url+"/name/"+country1).json()
pprint(name1)



request=requests.get(url).json()


