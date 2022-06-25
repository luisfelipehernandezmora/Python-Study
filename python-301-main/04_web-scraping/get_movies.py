"""The aim of these file is to show how to make an HTTP 
request and dump it into a json file for enquiry later"""

import requests
import json
import os

response = requests.get("https://ghibliapi.herokuapp.com/films").json()
movies_file=os.getcwd()+"/python-301-main/04_web-scraping/films.json" #give independence of the system where you run it

with open(movies_file,"w") as file:
    json.dump(response,file)
