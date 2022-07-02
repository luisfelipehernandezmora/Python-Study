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

#A json file with the cats names, don't have the full information 
initial_file=os.getcwd()+"/python-301-main/04_web-scraping/initial.json"

if os.path.isfile(initial_file)==False:
    url = "https://ghibliapi.herokuapp.com/species/603428ba-8a86-4b0b-a9f1-65df6abef3d3"
    cats_page=requests.get(url).json()
    with open(initial_file,"w") as file:
        json.dump(cats_page,file)

cats_file=os.getcwd()+"/python-301-main/04_web-scraping/bank_of_cats.json"

if os.path.isfile(cats_file)==False:
    with open(initial_file,"r") as file:
        urls_of_cats=json.load(file)["people"]

list_of_cats=[]
for each_url in urls_of_cats: #
    cat_req=requests.get(each_url).json()
    color=cat_req["hair_color"]
    eye_color=cat_req["eye_color"]
    name=cat_req["name"]
    gender=cat_req["gender"]
    each_cat=Cat(name,gender,color,eye_color)
    list_of_cats.append(each_cat)

list_of_cats
for i in list_of_cats:
    print(f"The cat {i.name} has {i.hair_color} hair and {i.eye_color} eyes and is {i.gender}")