import webbrowser
import requests
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

class Soup:
    "Creates a Soup from the given Ingredients"

    def __init__(self,name) :
        self.name=name

    def __str__(self) -> str:
        return(f"Soup({self.name})")

    def cook(self, *ingredients):
        """Takes Ingredients and Spices to cook a soup

        Args:
            args: Ingredients for the soup, as many as needed

        return: The possible recipes to cook with those ingredients, the amount of people who can eat 
        """
        for ing in ingredients:
            lista=list.append(ing)
        a=


# def look_recipe(lista):

#     url="https://api.spoonacular.com/recipes/findByIngredients?apiKey=f1727df4f2004de98168f2021f8f3c87&ingredients=apples,+flour,+sugar&number=2"