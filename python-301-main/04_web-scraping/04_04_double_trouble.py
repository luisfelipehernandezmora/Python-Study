# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.
import requests
import json 
from pprint import pprint
import webbrowser

"""This program asks about a musical artist and look up some informations about him/her and some 
information about the country as well, it can displays a Google Maps view from the country if desired"""

#1) Select an artist and research about  
ask=input(f"\nFrom which artist you will like to know about? (If it have spaces, put underscore instead) ")

url= f"https://theaudiodb.com/api/v1/json/2/search.php?s={ask}"
artist=requests.get(url).json()
#pprint(artist)

#2) For the sake of fewer requests, create a Json with the content of the request
folder="/Users/flormariamorafallas/Desktop/CodingNomads/Python-Study/python-301-main/04_web-scraping/artist.json"
with open(folder,"w") as file:
    json.dump(artist,file)

with open(folder,"r") as file:
    data=json.load(file)
#pprint(data)

#3) Make the Calls
name=data["artists"][0]["strArtist"]
nac=data["artists"][0]["intBornYear"]
stilo=data["artists"][0]["strStyle"]
country=data["artists"][0]["strCountry"]
country=str(country)
elems=country.split(", ")
# print(f"The country is {elems[1]}")
print(f"\n{name} is an artist from {country}, borned in {nac}. It's style of music is {stilo}.")
ask2=input(f'\nYou want to know more information about the country of {name}? ')
if ask2=="Yes" or ask2=="yes":
    # if elems[1] == "USA"
    url2=f"https://restcountries.com/v3.1/name/{elems[-1]}"
    info_country=requests.get(url2).json()
    folder="/Users/flormariamorafallas/Desktop/CodingNomads/Python-Study/python-301-main/04_web-scraping/country_info.json"
    with open(folder,"w") as file:
        json.dump(info_country,file)
    with open(folder,"r") as file:
        data2=json.load(file)

    population=data2[0]["population"]
    area=data2[0]["area"]
    maps=data2[0]["maps"]["googleMaps"]
    lang=data2[0]["languages"].values()
    langs=[]
    for x in lang:
        langs.append(x)
    langs=", ".join(langs)
    print(f"\n{elems[-1]} have a population of {population} habitants an of {area} km2 and the spoken language/s are {langs}")
# 4) Ask about displaying a map
    ask3=input(f"\nSince you are interested, you will like to see it in the map? ")  
    if ask3=="Yes" or "yes":
        webbrowser.open(maps,new=0, autoraise=True)
    else:
        print(f"Oh that's oh right! Thanks for using the program!")
        quit()
else:
    print(f"Oh that's oh right! Thanks for using the program!")