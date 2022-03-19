import json
import os
from pprint import pprint
import requests
import webbrowser
key=os.environ["keyspoon"]
num_rec=5
folder="/home/luisfelipe/Coding Nomads/python-301-main/03_inheritance/sample.json"
with open(folder,"r") as file: #Reads the json file already done (to minimize multiple unnecesary callings)
    recipe=json.load(file)

cooking_book={}
ids=[]
for i in range (5): #Maps the recipes availables and Id number
    title=recipe[i]["title"]
    recipe_id=recipe[i]["id"]
    missed_ingredients=recipe[i]["missedIngredients"]
    used_ingredients=recipe[i]["usedIngredients"]
    cooking_book[recipe_id]=title
    ids.append(recipe_id)
    print(f"This recipe is called {title} and have the id {recipe_id}")
    for i in range(len(missed_ingredients)):
        missed=missed_ingredients[i]["name"]
        #print(f"missed {missed}")
    for i in range(len(used_ingredients)):
        used=used_ingredients[i]["name"]
        #print(f"used {used}")

ask=input(f"You want to look for any of these recipes procedures? ") #This section looks for the recipe
if ask == "Yes":
    ask_id=int(input(f"Oh right! tell me the id of that recipe \n")) #The user choose which recipe to look upon
    if ask_id in ids:
        #https://api.spoonacular.com/recipes/782619/information?apiKey=f1727df4f2004de98168f2021f8f3c87&includeNutrition=false
        url="https://api.spoonacular.com/recipes/"+str(ask_id)+"/information?apiKey="+key+"&includeNutrition=false"
        pasos=requests.get(url).json()["instructions"]
        site=requests.get(url).json()["sourceUrl"]
        print(pasos,"\n")
        print("Voila Bonne Apettite you have now the full steps on how to proceed, salud! \n also let me open the webpage for you ... \n")
        webbrowser.open(site, new=0, autoraise=True)
else:
    print(f"ok, you have the recipes, just come back whenever you want ")
    
#url="https://api.spoonacular.com/recipes/findByIngredients?apiKey=key&ingredients=apples,+flour,+sugar&number=2"
