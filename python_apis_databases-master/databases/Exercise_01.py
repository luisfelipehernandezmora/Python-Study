'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''
import sqlalchemy
import pymysql
# import os

# user=os.environ("username")
# key=os.environ("mysql_pass")


engine=sqlalchemy.create_engine('mysql+pymysql://root:Sabanilla1:@localhost/sakila')
conection=engine.connect()
metadata=sqlalchemy.MetaData()
actor=sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
print(actor.columns.keys())

