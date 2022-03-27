# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5
from pprint import pprint
import requests
import json
BASE_URL = "https://pokeapi.co/api/v2/"
url="https://pokeapi.co/api/v2/pokemon/1/"
folder="/home/luisfelipe/Coding Nomads/python-301-main/04_web-scraping/temp_pokemon.json"
# pokemon=requests.get(url).json()
# with open(folder,"w") as file:
#     json.dump(pokemon,file)
with open(folder,"r") as file:
    data=json.load(file)
name=data["forms"]

# pprint(data)
# print(type(data))