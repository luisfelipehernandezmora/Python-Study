# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

url = "https://en.wikipedia.org/wiki/Web_scraping"
import requests
from bs4 import BeautifulSoup

folder="/Users/flormariamorafallas/Desktop/CodingNomads/Python-Study/python-301-main/04_web-scraping/wikipedia_articles"

page=requests.get(url).text
soup=BeautifulSoup(page, features="html.parser")

links=soup.find_all("a")
for link in links:
    print(link)
    #endpoint=link["href"]