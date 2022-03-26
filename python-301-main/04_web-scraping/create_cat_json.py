import requests
import json

url = "https://ghibliapi.herokuapp.com/species/603428ba-8a86-4b0b-a9f1-65df6abef3d3"
cats_page=requests.get(url).json()

folder="/home/luisfelipe/Coding Nomads/python-301-main/04_web-scraping/cats.json"
with open(folder,"w") as file:
    json.dump(cats_page,file)