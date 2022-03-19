import json
import os
import requests
key=os.environ["keyspoon"]
num_rec=5
folder="/home/luisfelipe/Coding Nomads/python-301-main/03_inheritance/sample.json"
with open(folder,"r") as file:
    recipe=json.load(file)

cooking_book={}

for i in range (5):
    title=recipe[i]["title"]
    recipe_id=recipe[i]["id"]
    cooking_book[recipe_id]=title
    print(f"This recipe is called {title} and have the id {recipe_id}")

ask=input(f"You want to look for any of these recipes procedures? ")
if ask == "Yes":
    ask_id=input(f"Oh right! tell me the id of that recipe ")
    if ask_id in cooking_book.values():
        url=f"https://api.spoonacular.com/recipes/"+{ask_id}+"/information?apiKey="+key+"&includeNutrition=false"
        
    
