import json
from pprint import pprint
from pathlib import Path

folder="/home/luisfelipe/Coding Nomads/python-301-main/03_inheritance/sample.json"

with open(folder,"r") as file:
    recipe=json.load(file)[0]
    title=recipe["title"]
pprint(recipe)
print(title)