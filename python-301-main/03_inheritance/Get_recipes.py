import json
import os
from pprint import pprint
import requests
import webbrowser
key=os.environ["keyspoon"]
num_rec=5
folder="/home/luisfelipe/Coding Nomads/python-301-main/03_inheritance/sample.json"
with open(folder,"r") as file:
    recipe=json.load(file)

cooking_book={}
ids=[]
for i in range (5):
    title=recipe[i]["title"]
    recipe_id=recipe[i]["id"]
    cooking_book[recipe_id]=title
    ids.append(recipe_id)
    print(f"This recipe is called {title} and have the id {recipe_id}")

ask=input(f"You want to look for any of these recipes procedures? ")
if ask == "Yes":
    ask_id=int(input(f"Oh right! tell me the id of that recipe "))
    if ask_id in ids:
        #https://api.spoonacular.com/recipes/782619/information?apiKey=f1727df4f2004de98168f2021f8f3c87&includeNutrition=false
        url="https://api.spoonacular.com/recipes/"+str(ask_id)+"/information?apiKey="+key+"&includeNutrition=false"
        pasos=requests.get(url).json()["instructions"]
        print(pasos)
        print("Voila Bonne Apettite you have now the full steps on how to proceed, salud!")
else:
    print(f"ok, you have the recipes, just come back whenever you want ")
    
