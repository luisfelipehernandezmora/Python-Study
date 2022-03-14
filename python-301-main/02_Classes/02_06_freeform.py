# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...
import requests
class Countries():
    """Class to define a country object and qualities asociate with it

    Args:
        1st arg: name
        2nd arg: population in million of people
        3rd arg: territorial extension
        4th arg: language     
                
    Returns:
        A country object with information of the countries in order: [name, population, area, language]
        """
    def __init__(self, name, population, territory, language):
        self.name=name
        self.population=population
        self.territory=territory
        self.language=language
    
    def __str__(self) -> str:
        return(f"Country({self.name} {self.population} {self.territory} {self.language})")
    
    def __str__(self) -> str:
        return(f"Country(name = {self.name}, population = {self.population} millions, territory = {self.territory} km2, languages = {self.language})")
        
    def __add__(self, other):
        new_name=self.name+" and "+other.name
        new_population=round(self.population+other.population,2)
        new_territory=self.territory+other.territory
        new_language=dict(self.language,**other.language)
        return(Countries(name=f"The union of {new_name}", population=new_population, territory=new_territory, language=new_language))

url="https://restcountries.com/v3.1"

country1=input("Which country you want to know about? ")
country2=input("Which other country you want to know about? ")
country3=input("Which other country you want to know about? ")

name1=requests.get(url+"/name/"+country1).json()[0]["name"]["common"]
name2=requests.get(url+"/name/"+country2).json()[0]["name"]["common"]
name3=requests.get(url+"/name/"+country3).json()[0]["name"]["common"]

if name1==country1:
    population1=requests.get(url+"/name/"+country1).json()[0]["population"]
    population1=round(population1/1000000,2)
    area1=requests.get(url+"/name/"+country1).json()[0]["area"]
    language1=requests.get(url+"/name/"+country1).json()[0]["languages"]
if name2==country2:
    population2=requests.get(url+"/name/"+country2).json()[0]["population"]
    population2=round(population2/1000000,2)
    area2=requests.get(url+"/name/"+country2).json()[0]["area"]
    language2=requests.get(url+"/name/"+country2).json()[0]["languages"]
if name3==country3:
    population3=requests.get(url+"/name/"+country3).json()[0]["population"]
    population3=round(population3/1000000,2)
    area3=requests.get(url+"/name/"+country3).json()[0]["area"]
    language3=requests.get(url+"/name/"+country3).json()[0]["languages"]

country1=Countries(name1,population1,area1,language1)
country2=Countries(name2,population2,area2,language2)
country3=Countries(name3,population3,area3,language3)
union1=country1+country2
union2=country3+country2
paises=[country1,country2,country3]

print(country1,"\n")
print(country2,"\n")
print(country3,"\n")
print(union1,"\n")
print(union2,"\n")

class Menu():
    """Class to define Menu items of a restaurant

    Args:
        1st arg: name
        2nd arg: veg or non veg 
        3rd arg: calories
        4th arg: price     
                
    Returns:
        A list of information of the country in order: [name, veg/non veg, calories, price]
        """  
    def __init__(self, name, type, calorie, price):
        self.name=name
        self.type=type
        self.calorie=calorie
        self.price=price
    
    def __str__(self) -> str:
        return(f"Menu({self.name} {self.type} {self.calorie} {self.price})")
    
    def __str__(self) -> str:
        return(f"Menu(Name = {self.name}, Type = {self.type}, Calorie content = {self.calorie}, Price = {self.price})")
    
    def __add__(self,other):
        new_name=f"{self.name} \n {other.name}"
        if self.type or other.type == "Non Veg":
            new_type="Non Veg"
        else:
            new_type="Vegetarian!"
        new_calorie=self.calorie+other.calorie
        new_price=self.price+other.price
        return(Menu(name=new_name, type=new_type, calorie=new_calorie, price=new_price))

    def create_item(item,type,calorie,price):
        """Function to introduce Menu items

        Args:
            1st arg: name
            2nd arg: veg or non veg 
            3rd arg: calories
            4th arg: price     
                    
        Returns:
        A list of information of the country in order: [name, veg/non veg, calories, price]
        """ 
        # item=input("What is the name of the item you want to create in the menu?")
        # type=input("Vegetarian or Non Veg?")
        # calorie=int(input("How many calories it have?"))
        # price=int(input("Price?"))
        return(Menu(item,type,calorie,price))

pancakes=Menu.create_item("Banana pancakes","Veg",300,3)
best_coffee=Menu.create_item("The best coffe in town","Veg",20,1.50)
sandwich=Menu.create_item("Kid's meal","Non Veg",300,4)
fruits=Menu.create_item("Fresh season fruit","Veg",200,3.75)

breakfast1=pancakes+best_coffee+fruits
breakfast2=sandwich+best_coffee+fruits

print(pancakes,"\n")
print(best_coffee,"\n")
print(sandwich,"\n")
print(fruits,"\n")
print(breakfast1,"\n")
print(breakfast2,"\n")