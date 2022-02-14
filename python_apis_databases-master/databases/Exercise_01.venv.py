'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''
import sqlalchemy
import os
from pprint import pprint

user=os.environ["username"]
key=os.environ["mysql_pass"]

engine=sqlalchemy.create_engine('mysql+pymysql://'+user+':'+key+'@localhost/sakila')
conection=engine.connect()
metadata=sqlalchemy.MetaData()
actor=sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
film=sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
category=sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)

actors=sqlalchemy.select([actor])
movies=sqlalchemy.select([film])
categories=sqlalchemy.select([category])

# result_proxy=conection.execute(actors)
# result_set=result_proxy.fetchall()
# pprint(result_set)
result_proxy=conection.execute(movies)
result_set=result_proxy.fetchall()
pprint(result_set)
result_proxy=conection.execute(categories)
result_set=result_proxy.fetchall()
pprint(result_set)
