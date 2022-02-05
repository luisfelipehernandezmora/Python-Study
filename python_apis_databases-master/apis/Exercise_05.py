'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''
from pprint import pprint
import requests

url="http://demo.codingnomads.co:8080/tasks_api/users"
id=input("Enter your user Id that you will be deleting: ")

#Here You delete that register
request=requests.delete(url+"/"+id)

#Here to verify all is correct
request=requests.get(url).json()
pprint(request)