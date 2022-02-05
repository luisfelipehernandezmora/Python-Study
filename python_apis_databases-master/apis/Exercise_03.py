'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''
import requests
from pprint import pprint

url="http://demo.codingnomads.co:8080/tasks_api/users"

name=input("Enter your name: ")
last_name=input("Enter your last name: ")
email=input("Enter your email adress: ")

body={
    "first_name": name,
    "last_name": last_name,
    "email": email
}
request=requests.post(url, json=body)

request=requests.get(url).json()
pprint(request)
