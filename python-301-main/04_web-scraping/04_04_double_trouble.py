# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.
import requests
import json 
from pprint import pprint

#1) Select an artist and research about  
ask=input(f"From which artist you will like to know about? ")

url= f"https://theaudiodb.com/api/v1/json/2/search.php?s={ask}"
artist=requests.get(url).json()
#pprint(artist)

#2) For the sake of fewer requests, create a Json with the content of the request
folder="/Users/flormariamorafallas/Desktop/CodingNomads/Python-Study/python-301-main/04_web-scraping/artist.json"
# with open(folder,"w") as file:
#     json.dump(artist,file)

with open(folder,"r") as file:
    data=json.load(file)
#pprint(data)

#3) Make the Calls
name=data["artists"][0]["strArtist"]
print(name)
