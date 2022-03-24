import requests

url="https://codingnomads.github.io/recipes/"
page=requests.get(url)
print(page.text)