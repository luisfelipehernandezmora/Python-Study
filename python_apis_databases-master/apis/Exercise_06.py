'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''

import requests
from pprint import pprint
from datetime import datetime

hi=int(input("""Hello user, please select from the menu, what you will like to do:
1) Create a new account 
2) View all your tasks 
3) View your completed tasks 
4) View only your incomplete tasks 
5) Create a new task 
6) Update an existing task 
7) Delete a task 
"""))
if hi==1:
    url="http://demo.codingnomads.co:8080/tasks_api/users" 
    name=input("Please provide your name: ")
    last_name=input("Please provide your last name: ")
    email=input("Please provide your email for the account: ")
    body={
        "first_name":name,
        "last_name":last_name,
        "email":email
    }
    response=requests.post(url,json=body)
    if response.status_code==200:
        response=requests.get(url)
        data=response.json()
        #print(f"So you want to make an account, it's done correctly, look! {requests.get(url).text}")
        d=data["data"][-1]
        pprint(f"So you want to make an account, it's done correctly, look! {d}")

elif hi==2:
    url="http://demo.codingnomads.co:8080/tasks_api/tasks"
    response=requests.get(url)
    data=response.json()
    largo=data["data"]
    pprint(largo)

elif hi==3:
    url="http://demo.codingnomads.co:8080/tasks_api/tasks"
    response=requests.get(url)
    data=response.json()
    largo=data["data"]
    for x in range(len(largo)):
        status=largo[x]["completed"]
        id=largo[x]["id"]
        if status==True:
            print(f"The id {id} is complete ({status})")

elif hi==4:
    url="http://demo.codingnomads.co:8080/tasks_api/tasks"
    response=requests.get(url)
    data=response.json()
    largo=data["data"]
    for x in range(len(largo)):
        status=largo[x]["completed"]
        id=largo[x]["id"]
        if status==False:
            print(f"The id {id} is incomplete ({status})")

elif hi==5:
    url="http://demo.codingnomads.co:8080/tasks_api/tasks"
    completed=input("Your task will be complete or no? ")
    if completed=="yes":
        status=True
    else:
        status=False
    created=str(datetime.now())
    description=input("Put a description here: ")
    id=int(input("Tell your Id: "))
    userid=int(input("Tell your User Id: "))
    name=input("Your name? ")
    body ={
        "completed": status,
        "createdAt": created,
        "description": description,
        "id": id,
        "name": name,
        "updatedAt": created,
        "userId": userid
    }
    response = requests.post(url, json=body)
    print(f"Response Content: {response.content}")
    response=requests.get(url)
    pprint(f"Response Content: {response.content}")

elif hi==6:
    url="http://demo.codingnomads.co:8080/tasks_api/tasks"
    id=int(input("Tell your Id: "))
    completed=input("Your task will be complete or no? ")
    if completed=="yes":
        status=True
    else:
        status=False
    created=str(datetime.now())
    description=input("Put a description here: ")
    userid=int(input("Tell your User Id: "))
    name=input("Your name? ")
    body ={
        "completed": status,
        "createdAt": created,
        "description": description,
        "id": id,
        "name": name,
        "updatedAt": created,
        "userId": userid
    }
    response = requests.put(url, json=body)
    print(f"Response Content: {response.content}")
    response=requests.get(url)
    pprint(f"Response Content: {response.content}")

elif hi==7:
    id=input("Insert the id you want to delete ")
    num="/"+id
    print(num)
    url="http://demo.codingnomads.co:8080/tasks_api/tasks"
    response=requests.delete(url+num)