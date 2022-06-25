# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.herokuapp.com/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.


import os
import json
from pprint import pprint
import requests
class Cat:
    """Class to define a Studio Ghibli cat

    Args:
        1st arg: name
        2nd arg: gender 
        3rd arg: hair color
        4th arg: eye color     
                
    Returns:
        A list of information of the cat in order: [name, gender, hair color, eye color]
        """
    def __init__(self,name,gender,hair_color,eye_color):
        self.name=name
        self.gender=gender
        self.hair_color=hair_color
        self.eye_color=eye_color

    def __str__(self) -> str:
        return(f"Cat(name={self.name},gender={self.gender},hair_color={self.hair_color},eye_color={self.eye_color})")

cats_file=os.getcwd()+"/python-301-main/04_web-scraping/cats.json"

if os.path.isfile(cats_file)==False:
    url = "https://ghibliapi.herokuapp.com/species/603428ba-8a86-4b0b-a9f1-65df6abef3d3"
    cats_page=requests.get(url).json()
    with open(cats_file,"w") as file:
        json.dump(cats_page,file)





folder2=os.getcwd()+"/python-301-main/04_web-scraping/cat_temp_info.json"
folder3=os.getcwd()+"/python-301-main/04_web-scraping/Studio_Ghibli_cats.txt"

with open(cats_file,"r") as file:
    data=json.load(file)["people"]
book_of_cats=[]
#pprint(data)
for cat in data:
    cat_info=requests.get(cat).json()
    with open(folder2,"w") as file:
        json.dump(cat_info,file)
    with open(folder2,"r") as file:
        cat_data=json.load(file)
    #pprint(cat_data)
    name=cat_data["name"]
    gender=cat_data["gender"]
    hair_color=cat_data["hair_color"]
    eye_color=cat_data["eye_color"]
    new_cat=Cat(name,gender,hair_color,eye_color)
    book_of_cats.append(new_cat) #Adopt the cat in your book :D!

for cat in book_of_cats:
    print(cat)
    with open(folder3,"a") as file:
        file.write(cat.__str__()+"\n")