'''
Using the requests package, make a GET request to the api behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users

Print out:

    - the status code
    - the encoding of the response
    - the text of the response body
'''
import requests
from pprint import pprint

url='http://demo.codingnomads.co:8080/tasks_api/users'
request=requests.get(url)
codigo=request.status_code
texto=request.json()
print("the status code is",codigo)
pprint(texto)