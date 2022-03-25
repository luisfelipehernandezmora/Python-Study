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

def look_recipe(recipe):
    new_recipe=requests.get(recipe).text
    soup=BeautifulSoup(new_recipe,features="html.parser")
    title=soup.find("h1",class_="title").text
    author=soup.find("p",class_="author").text
    body=soup.find("div",class_="md").text
    return(title,author,body)

# for link in links:
#     endpoint=link["href"]
#     #print(endpoint)
#     recipe=url+endpoint
#     new_link.append(recipe)
#     print(f"The link for the new recipe is {recipe}")
    

a="https://codingnomads.github.io/recipes/recipes/68-kimchi-fried-rice-wi.html"
b=look_recipe(a)
print(b[2])


