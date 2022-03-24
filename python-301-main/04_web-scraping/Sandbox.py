import requests
from bs4 import BeautifulSoup

url="https://codingnomads.github.io/recipes/"
url2="https://codingnomads.github.io/recipes/recipes/68-kimchi-fried-rice-wi.html"
page=requests.get(url2).text
#print(page,type(page))

soup=BeautifulSoup(page,features="html.parser")
print(soup.prettify)

# links=soup.find_all("a")
# for link in links:
#     print(link["href"])