'''
Using the PokéAPI https://pokeapi.co/docs/v2#pokemon-section
fetch the name and height of all 151 Pokémon of the main series.

Create a text document that describes each Pokémon using the information
available in the JSON response.
NOTE: only using 'height' is enough, but if you want more, go crazy.

BONUS: Using your script, create a folder and download the main 'front_default'
       sprites for each Pokémon using requests into that folder.
       Name the files appropriately using the name data from your response.

'''
import requests
from pprint import pprint

url="https://pokeapi.co/api/v2/pokemon/"
for num in range(1,20):
       height=requests.get(url+str(num)).json()["height"]
       name=requests.get(url+str(num)).json()["name"]
       print(name,height)
       with open("Pokemon.txt","a") as file:
              file.write(f"{name}'s height is {height}")
              file.write("\n")



