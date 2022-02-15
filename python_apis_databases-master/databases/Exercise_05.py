'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''
import sqlalchemy
import os
from pprint import pprint
import requests
import sqlalchemy_utils

#Get the information from the API
url="http://demo.codingnomads.co:8080/tasks_api/tasks"
response=requests.get(url)
data=response.json()["data"]
users={}
lista=[]
existing_values=[]
for i in data:
    c=i["id"]
    b=i["name"]
    e=i["userId"]
    existing_values.append(c) #This will save all the existing records to don't overwrite anything
    print(f"Task id: {c} and task: {b} on User id {e}")
    users["Task_id"]=c
    users["Task"]=b
    users["User_id"]=e
    lista.append(users)
    users={}

#Going in to the DB and create a Table
user=os.environ["username"]
key=os.environ["mysql_pass"]
engine = sqlalchemy.create_engine('mysql+pymysql://'+user+':'+key+'@localhost/GoodDB')
conection=engine.connect()
metadata=sqlalchemy.MetaData()

query=sqlalchemy.Table("API_tasks_info_CodNom", metadata, 
        sqlalchemy.Column("Task_id",sqlalchemy.Integer(),primary_key=True),
        sqlalchemy.Column("Task",sqlalchemy.String(255)),
        sqlalchemy.Column("User_id",sqlalchemy.Integer())
    )
metadata.create_all(engine)
use_table=sqlalchemy.Table("API_tasks_info_CodNom", metadata, autoload=True, autoload_with=engine)

#Before passing the information, we want to know if the task already exists
for elem in lista:
    a=elem["Task_id"]
    if a in existing_values:
        lista.remove(elem)
        
if len(lista)==0:
    print("Nothing to add, all is up-to-date")
    quit()

values=lista #We need a list of dictionaries
query=sqlalchemy.insert(use_table)
response_proxy=conection.execute(query,values)