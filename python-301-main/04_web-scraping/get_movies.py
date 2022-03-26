"""The aim of these file is to show how to make an HTTP 
request and dump it into a json file for enquiry later"""

import requests
import json

response = requests.get("https://ghibliapi.herokuapp.com/films").json()
folder="/home/luisfelipe/Coding Nomads/python-301-main/04_web-scraping/films.json"

with open(folder,"w") as file:
    json.dump(response,file)
