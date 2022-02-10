# Add an API call to your CLI game that assigns a name to your player.
import requests

url="https://uzby.com/api.php?min=4&max=10"
response=requests.get(url).text
print(response)