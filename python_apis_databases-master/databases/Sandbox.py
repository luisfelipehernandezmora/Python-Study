'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''
import sqlalchemy
import os
from pprint import pprint
import sqlalchemy_utils


#Keep your (strong) mysql password safe 
user=os.environ["username"]
key=os.environ["mysql_pass"]

engine = sqlalchemy.create_engine('mysql+pymysql://'+user+':'+key+'@localhost/GoodDB')
conection=engine.connect()
metadata=sqlalchemy.MetaData()

Users=sqlalchemy.Table('Users',metadata,autoload=True,autoload_with=engine)
a=Users.columns.keys()
print(a, type(a))



# response_proxy=conection.execute(query)