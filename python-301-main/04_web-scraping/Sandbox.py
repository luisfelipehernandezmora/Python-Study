import requests
import json
from pprint import pprint

response = requests.get("https://ghibliapi.herokuapp.com/films").json()
pprint(response.json())