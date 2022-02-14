'''
Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:

    - create at least 3 tables
    - insert data to each table
    - update data in each table
    - select data from each table
    - delete data from each table
    - use at least one join in a select query

BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!
'''
import sqlalchemy
import os
from pprint import pprint
import sqlalchemy_utils

#Keep your (strong) mysql password safe 
user=os.environ["username"]
key=os.environ["mysql_pass"]

#Create the new DB and make sure to create it only once with the if statement
engine = sqlalchemy.create_engine('mysql+pymysql://'+user+':'+key+'@localhost/GoodDB')
if not sqlalchemy_utils.database_exists(engine.url):
    sqlalchemy_utils.create_database(engine.url)
# print(sqlalchemy_utils.database_exists(engine.url)) ## To verify the DB is existing properly

conection=engine.connect()
metadata=sqlalchemy.MetaData()

question=int(input("""What do you wnat to do? 
1) Create a table
2) Insert data to a table
3) Update data in a table
4) Select data from a table
5) Delete data from a table
6) Use at least one join in a select query ##Think how to rename this lines ***
"""))

if question ==1:
    name=input("So, What is gonna be the name of your table? ")
    cols=int(input("How many columns you want to put? "))
    cols_names=[]
    for i in range(cols):
        name_col=input(f"Write the name of the {i} column ")
        cols_names.append(name_col)
        i+=1
    for x in cols_names:
        query=sqlalchemy.Table(name, metadata, sqlalchemy.Column(x))
    metadata.create_all(engine)