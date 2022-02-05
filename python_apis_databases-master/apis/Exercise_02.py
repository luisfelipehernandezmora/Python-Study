'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''
from distutils import core
import requests
from pprint import pprint

url='http://demo.codingnomads.co:8080/tasks_api/users'
request=requests.get(url)
codigo=request.status_code
texto=request.json()["data"]
correos=[]
for x in texto:
    correos.append(x["email"])
pprint(correos)