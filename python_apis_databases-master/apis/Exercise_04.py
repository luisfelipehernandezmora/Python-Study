'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests
from pprint import pprint

#These will be updating information for an already existing user
name=input("Enter your name: ")
last_name=input("Enter your last name: ")
email=input("Enter your email adress: ")

#We make a new body, to insert the information as a new register
body={
    "first_name": name,
    "last_name": last_name,
    "email": email
}
#With the Id we will know which user to modify
id=input("Enter your user Id that you will be modyfing: ")

#Make the PUT request, important the "/" symbol in the ID
url="http://demo.codingnomads.co:8080/tasks_api/users"
request=requests.put(url+"/"+id, json=body)

#Check all went fine by printing here itself
request=requests.get(url).json()
pprint(request)