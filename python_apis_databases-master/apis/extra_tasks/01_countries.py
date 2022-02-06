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

name1=requests.get(url+"/name/"+country1).json()[0]["name"]["common"]

if name1 == country1:
    population1=requests.get(url+"/name/"+country1).json()[0]["population"]
    area1=requests.get(url+"/name/"+country1).json()[0]["area"]

name2=requests.get(url+"/name/"+country2).json()[0]["name"]["common"]
if name1 == country1:
    population2=requests.get(url+"/name/"+country2).json()[0]["population"]
    area2=requests.get(url+"/name/"+country2).json()[0]["area"]

if population1>population2:
    print(f"{country1} have a bigger population than {country2}, {population1} against {population2}")
else:
    print(f"{country2} have a bigger population than {country1}, {population2} against {population1}")

if area1>area2:
    print(f"{country1} have a bigger territory than {country2}, {area1} against {area2}")
else:
    print(f"{country2} have a bigger territory than {country1}, {area2} against {area1}")
