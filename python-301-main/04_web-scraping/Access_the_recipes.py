import requests
from bs4 import BeautifulSoup

#Scrape the idnex page and get all the links
url="https://codingnomads.github.io/recipes/"
page=requests.get(url).text
#print(recipe)
soup=BeautifulSoup(page,features="html.parser")
links=soup.find_all("a")
new_link=[]
folder="/home/luisfelipe/Coding Nomads/python-301-main/04_web-scraping/recipes"
book={}
def look_recipe(recipe):
    """Function to scape a specific recipe

    Args:
        1st arg: url of the endpoint recipe 
                
    Returns:
    The title, the author and the instructions to cook. It can be accessby indexes
    """ 
    new_recipe=requests.get(recipe).text
    soup=BeautifulSoup(new_recipe,features="html.parser")
    title=soup.find("h1",class_="title").text
    author=soup.find("p",class_="author").text
    body=soup.find("div",class_="md").text
    print(f"The recipe in this link is {title} \n")
    print(f"Created {author} \n")
    print(f"And the steps to cook are \n {body} \n")
    return(title,author,body)

for link in links:
    endpoint=link["href"]
    comon=link.text
    recipe=url+endpoint
    new_link.append(recipe)
    print(comon)
    book[comon]=recipe
ask=input(f"\n\nSo you have all the available recipes, copy and paste the like of the one you will like to look for! ")   
#print(book[ask])
if ask in book.keys():
    print(f"So the recipe you choose is: \n.\n.\n.")
    receta=look_recipe(book[ask])