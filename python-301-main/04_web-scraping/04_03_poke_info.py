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
import os

class pokemon:
    """Class to define Pokemons!

    Args:
        1st arg: name
        2nd arg: number
        3rd arg: types 
                
    Returns:
        A list of information of the Pokemon in order: [name, number, types]
        """
    def __init__(self,name,number,types):
        self.name=name
        self.number=number
        self.types=types
    def __str__(self) -> str:
        return(f"Pokemon(name={self.name}, number={self.number}, types={self.types})")

BASE_URL = "https://pokeapi.co/api/v2/"
url="https://pokeapi.co/api/v2/pokemon/1/"
pokedex=[]
folder=os.getcwd()+"/python-301-main/04_web-scraping/temp_pokemon.json"
def list_of_pokemons():
    """Creates a list of all the urls to access each pokemon, the user will give an input of how 
    many pokemons wants to look for

    Returns:
        A list of of all the urls to access each pokemon
        """
    ask=input(f"How many pokemons you want to look for? ")
    if int(ask)>40 or int(ask)<10:
        ask=40
        ask=str(ask)
    url_many=f"https://pokeapi.co/api/v2/pokemon/?offset=0&limit="+ask
    list_of_all_pokemons=requests.get(url_many).json()["results"]
    list_of_urls=[]
    for i in list_of_all_pokemons:
        data2=i["url"]
        list_of_urls.append(data2)
    return(list_of_urls)

def create_pokemon_record(url):
    """Function to create a temporary json file in the computer and fetch from there

    Args:
        1st arg: url of the pokemon
                
    Returns:
        Nothing. It just creates a file in a particular location that the function 'look for pokemon' will use
        """
    folder=os.getcwd()+"/python-301-main/04_web-scraping/temp_pokemon.json"
    pokemons=requests.get(url).json()
    with open(folder,"w") as file:
        json.dump(pokemons,file)
    return(None)

def look_for_pokemon():
    """looks into a json file created by 'create_pokemon_record' to get the information from a particular pokemon
                
    Returns:
        A pokemon object
        """
    folder=os.getcwd()+"/python-301-main/04_web-scraping/temp_pokemon.json"
    with open(folder,"r") as file:
        data=json.load(file)
    name=data["forms"][0]["name"]
    number=data["id"]
    types=data["types"] 
    tipos=[]
    for i in types:
        dato=i["type"]["name"]
        tipos.append(dato)
    # print(name)
    # print(number)
    # print(tipos)
    poke=pokemon(name,number,tipos)
    return(poke)


lista_pokemones=list_of_pokemons()
#pprint(lista_pokemones)
for url in lista_pokemones:
    create_pokemon_record(url)
    pokemon2=look_for_pokemon()
    pokedex.append(pokemon2.__str__())
pprint(pokedex)