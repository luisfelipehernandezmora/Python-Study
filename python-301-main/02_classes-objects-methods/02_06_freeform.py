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
from turtle import update
import requests
from pprint import pprint
class Countries():
    """Class to define a country object and qualities asociate with it

    Args:
        1st arg: name
        2nd arg: population in million of people
        3rd arg: territorial extension
        4th arg: language     
                
    Returns:
        A list of information of the country in order: [name, population, area, language]
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
        new_population=self.population+other.population
        new_territory=self.territory+other.territory
        new_language=update(self.language,other.language)
        return(Countries(name=f"The union of those 2 countries is like:", population=new_population, territory=new_territory, language=new_language))


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


print(country1)
print(country2)
print(country3)
print(union1)
print(union2)
