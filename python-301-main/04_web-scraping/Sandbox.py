import requests
from bs4 import BeautifulSoup
from pprint import pprint

# # from the index get the links
# url="https://codingnomads.github.io/recipes/"
# page=requests.get(url).text
# # print(page)
# soup=BeautifulSoup(page,features="html.parser")
# links=soup.find_all("a")
# for link in links:  #Get HTML's here
#     print(link["href"])

# Get the Title, author and text describing the recipe
url2="https://codingnomads.github.io/recipes/recipes/68-kimchi-fried-rice-wi.html"
page=requests.get(url2).text
soup=BeautifulSoup(page,features="html.parser")
#print(soup.prettify)
#print(soup)
title=soup.find("h1",class_="title").text
author=soup.find("p",class_="author").text
body=soup.find("div",class_="md").text
# print(f"The recipe in this link is {title} \n")
# print(f"Created {author} \n")
# print(f"And the steps to cook are \n {body} \n")
