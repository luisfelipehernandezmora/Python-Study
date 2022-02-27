# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.
import requests
import pathlib
def name_gen():
    """Function to find random names

    Args:
        None
        
    Returns:
        A random name
    """
    url="https://uzby.com/api.php?min=4&max=10" #Get a random name for the user
    name=requests.get(url).text
    return(name)

def country_info():
    """Function to find the area and population of a requested country by the user

    Args:
        None, it will be an input question
        
    Returns:
        Population and area (in km2) from a country
    """
    url="https://restcountries.com/v3.1"
    country1=input(f"From which country is {name_gen()}? ")
    name1=requests.get(url+"/name/"+country1).json()[0]["name"]["common"]
    if name1 == country1:
        population1=requests.get(url+"/name/"+country1).json()[0]["population"]
        area1=requests.get(url+"/name/"+country1).json()[0]["area"]
    return(f"""So your fantasy character {name_gen()}, is from a fabolus country! {name1} what a delight! 
It's population is {population1} and the area of {name1} is {area1} km2""")

def writer():
    folder=pathlib.Path("/home/luisfelipe/Coding Nomads/python-201-main/04_functions-and-scopes/fiction.txt")
    text=country_info()
    with open (folder,"w") as file:
        file.write(text)
    return(None)

a=writer() #Go and check the direction in "folder"