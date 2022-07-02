# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

url = "https://en.wikipedia.org/wiki/Web_scraping"
import requests
from bs4 import BeautifulSoup
from random import randint
import os

def wikipedia_article(link):
    """Function to determine if a hyperlink goes to a wikipedia article

    Args:
        1st arg: url of the link
                
    Returns:
    True if the link goes to a wikipedia article
    """ 
    flag=False
    if link[:6]=="/wiki/":
        flag=True
    return flag

folder=os.getcwd()+"/python-301-main/04_web-scraping/wikipedia_articles/random_wiki_art.txt"
page=requests.get(url).text
soup=BeautifulSoup(page, features="html.parser")
links=soup.find_all("a")
wiki_arts=[]

for link in links:
    #print(link,'\n')
    endpoint=str(link.get('href'))
    if wikipedia_article(endpoint):
        link2="https://en.wikipedia.org"+endpoint
        wiki_arts.append(link2)
        #print(endpoint)

num=randint(0,len(wiki_arts)-1)

for i in wiki_arts:
    print(i)

mine=requests.get(wiki_arts[num]).text
with open (folder,"w") as file:
    file.write(mine)

print(f"\n Thank you!")