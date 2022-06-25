import requests
from bs4 import BeautifulSoup
from pprint import pprint

"-------------------------1---------------------"
first_url="https://codingnomads.github.io/recipes/"
page=requests.get(first_url).text
soup=BeautifulSoup(page,features="html.parser")

links=[]
all_the_links=soup.find_all("a")
for each_link in all_the_links:
    links.append(each_link["href"])  

ask=input(f"The available recipes are:\n{pprint(links)}\nwhich one you will like to open? ")

"-------------------------2---------------------"
# url="https://codingnomads.github.io/recipes/recipes/68-kimchi-fried-rice-wi.html"
url=first_url+ask

page=requests.get(url)
soup=BeautifulSoup(page.text)
# print(soup.prettify)

title=soup.find("h1",class_="title").text
author=soup.find("p",class_="author").text
recipe=soup.find("div",class_="md").text

line=f"The recipe {title} is made {author}\nthe recipe is {recipe}"
print(line)



"-------------------------3---------------------"


