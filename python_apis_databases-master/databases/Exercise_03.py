'''
Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.

'''
import sqlalchemy
import os
user=os.environ["username"]
key=os.environ["mysql_pass"]

engine=sqlalchemy.create_engine('mysql+pymysql://'+user+':'+key+'@localhost/sakila')
conection=engine.connect()
metadata=sqlalchemy.MetaData()

film=sqlalchemy.Table('film',metadata,autoload=True,autoload_with=engine)

query=sqlalchemy.update(film).values(rental_duration=10).where(film.columns.length>150)
response_proxy=conection.execute(query)