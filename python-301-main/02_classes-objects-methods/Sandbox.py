from ast import In
from unicodedata import name


class Ingredient():
    """Models the food item as an ingredient"""
    def __init__(self,name, amount):
        self.name=name
        self.amount=amount
    def expire(self):
        """Expires the ingredient"""
        print(f"Oh no! these {self.name} got expired!")
        self.name="expired" +self.name +":/" #Here you change the name from tomatoes to expired tomatoes
    def __str__(self):
        return(f"{self.name}({self.amount})")


papas=Ingredient("potatoes",5)
cookies=Ingredient("cookies",2)
water=Ingredient("Special water",3)

print("",papas.name,papas.amount,"\n",cookies.name,cookies.amount,"\n",water.name,water.amount)