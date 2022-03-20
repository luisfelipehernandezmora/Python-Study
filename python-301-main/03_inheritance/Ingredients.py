import webbrowser
import requests
from pprint import pprint
import json
import os
key=os.environ["keyspoon"]
import ctypes  # An included library with Python install.

class Ingredient:
    """Models the food item as an ingredient"""
    def __init__(self,name, amount):
        self.name=name
        self.amount=amount

    def expire(self):
        """Expires the ingredient"""
        print(f"Oh no! these {self.name} got expired!")
        self.name="expired " +self.name +" :/" #Here you change the name from tomatoes to expired tomatoes
    
    def __str__(self):
        return(f"{self.name} ({self.amount})")
        #return(f"There are {self.amount} {self.name}")
    
    def __repr__(self):
        return(f"Ingredient(name={self.name},amount={self.amount})")
    
    def __add__(self , other):
        """Combine two ingredients"""
        new_name = self.name + other.name
        new_amount=self.amount + other.amount
        return (Ingredient(name=new_name, amount=new_amount))

    def get_info(self):
        """Make a wikipedia search for this ingredient and open the page"""
        url="https://en.wikipedia.org/wiki/"+self.name
        webbrowser.open(url, new=0, autoraise=True)

class Spice(Ingredient):
    """Model a spice to flavor the food!"""

    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste=taste

    def expire(self):
        if self.name=="salt":
            print(f"Nonono, salt don't expire")
            return(None)
        elif self.name !="salt":
            print(f"Your {self.name} is expired, probably still good to use")
            self.name="old"+self.name

# class Soup(Ingredient):
#     "Creates a Soup from the given Ingredients"

#     def cook(self, *ingredients):
#         """Takes Ingredients and Spices to cook a soup

#         Args:
#             args: Ingredients for the soup, as many as needed

#         return: The possible recipes to cook with those ingredients, the amount of people who can eat 
#         """
#         list_of_food=[]
#         for ing in ingredients:
#             ing=self.name
#             list_of_food.append(ing)
        
#         look_recipe(list_of_food)
#         get_recipe()
#         return(None)
            

def look_recipe(lista):
    """Takes Ingredients list and look up for 5 possible recipes based on the ingredients recieved

    Args:
        args: A list of ingredients names available to cook

    return: The possible recipes to cook with those ingredients
    """
    key=os.environ["keyspoon"]
    url="https://api.spoonacular.com/recipes/findByIngredients?apiKey="+key+"&ingredients="
    for ing in lista:
       url+=ing+",+"
    url=url[:-2]
    url=url+"&number=5" #Get this amount of recipes
    
    recipes=requests.get(url).json()
    json_object=json.dumps(recipes,indent=4)
    folder="/home/luisfelipe/Coding Nomads/python-301-main/03_inheritance/5_recipes.json"
    with open(folder,"w") as outfile:
        outfile.write(json_object)

    return(recipes)
    
def get_recipe():
    """Looks up in json created to extract 

    Args:
        None, it uses an specific file

    return: The possible recipes to cook with those ingredients, the amount of people who can eat 
    """
    folder="/home/luisfelipe/Coding Nomads/python-301-main/03_inheritance/5_recipes.json"
    with open(folder,"r") as file: #Reads the json file already done (to minimize multiple unnecesary callings)
        recipe=json.load(file)

    ids=[]
    for i in range (5): #Maps the recipes availables and Id number
        title=recipe[i]["title"]
        recipe_id=recipe[i]["id"]
        ids.append(recipe_id)
        print(f"This recipe is called {title} and have the id {recipe_id}")

    ask_id=int(input(f"Oh right! tell me the id of that recipe ")) #The user choose which recipe to look upon
    if ask_id in ids:
        url="https://api.spoonacular.com/recipes/"+str(ask_id)+"/information?apiKey="+key+"&includeNutrition=false"
        pasos=requests.get(url).json()["instructions"]
        site=requests.get(url).json()["sourceUrl"]
        #Mbox(f"Steps of recipe {title}", pasos, 0)
        print(f"PRUEBA {pasos} \n")
        print(f"Voila Bonne Apettite you have now the full steps on how to proceed, salud! \n also let me open the webpage for you ... \n")
        webbrowser.open(site, new=0, autoraise=True)
    else:
        print(f"You didn't gave an id number of the given list \n")
        get_recipe()

# def Mbox(title, text, style):
    #  Styles:
    #  0 : OK
    #  1 : OK | Cancel
    #  2 : Abort | Retry | Ignore
    #  3 : Yes | No | Cancel
    #  4 : Yes | No
    #  5 : Retry | Cancel 
    #  6 : Cancel | Try Again | Continue
    # return (ctypes.windll.user32.MessageBoxW(0, text, title, style))
    

class Meal(Ingredient):
    "Creates a Soup from the given Ingredients"

    def cook():
        """Takes Ingredients and Spices to cook a soup

        Args:
            args: Ingredients for the soup, as many as needed

        return: The possible recipes to cook with those ingredients, the amount of people who can eat 
        """
        print(f"Hello! Welcome to this python cooking project! \n")
        lista=[]
        while True:
            ing=input(f"Which are the ingredients? (When finished type 'Done') ")
            if ing=="Done":
                print(f"Ok, let's cook it!")
                break
            quant=int(input(f"How many grams of {ing} you will add? "))
            is_spice=input(f"Is this a Spice (type 'Yes'), or not? ")
            if is_spice=="Yes":
                taste=input(f"Which is the taste of the spice? ")
                ing=Spice(ing,quant,taste)
            else:
                ing=Ingredient(ing,quant)
            lista.append(ing)
        print(f"Ok, you are done with the ingredients, you have: {lista}")

        weight=0

        for elem in lista:
            unit=elem.amount
            weight+=unit
        portions=int(weight/225) #225 grams or 8 oz. is the average soup portion size 
        print(f"\n\nSo you have food for {portions} people\n")

        names=[]
        for elem in lista:
            names.append(elem.name)
        print(names)

        look_recipe(names)
        get_recipe()