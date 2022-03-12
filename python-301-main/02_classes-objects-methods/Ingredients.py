import webbrowser
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

    def expire(self):
        if self.name=="salt":
            print(f"Nonono, salt don't expire")
            return(None)
        elif self.name !="salt":
            print(f"Your {self.name} is expired, probably still good to use")
            self.name="old"+self.name

lentils=Spice("Lentils",5)
lentils.expire()
print(lentils)

if __name__=="main":

    papas=Ingredient("potatoes",5)
    cookies=Ingredient("cookies",2)
    water=Ingredient("Special water",3)
    zanahorias=papas+cookies
    print("",papas.name,papas.amount,"\n",cookies.name,cookies.amount,"\n",water.name,water.amount,"\n",zanahorias.name,zanahorias.amount)
    print(papas)
    print(zanahorias)

mushrooms=Ingredient("Portobelo", 10)
cinnammon=Spice("Cinamon",1)
#salt=Spice("salt",2)
salt=Ingredient("salt",2)
mushrooms.expire()
cinnammon.expire()
salt.expire()