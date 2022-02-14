'''
Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

- Select all the actors with the first name of your choice

- Select all the actors and the films they have been in

- Select all the actors that have appeared in a category of a comedy of your choice

- Select all the comedic films and sort them by rental rate

- Using one of the statements above, add a GROUP BY statement of your choice

- Using one of the statements above, add a ORDER BY statement of your choice

'''
from unicodedata import category
import sqlalchemy
import os
from pprint import pp, pprint

user=os.environ["username"]
key=os.environ["mysql_pass"]

engine=sqlalchemy.create_engine('mysql+pymysql://'+user+':'+key+'@localhost/sakila')
metadata=sqlalchemy.MetaData()
conection=engine.connect()
question=int(input("""What you will like to do? 
1) Select all the actors with the first name of your choice
2) Select all the actors and the films they have been in
3) Select all the actors that have appeared in a category of your choice
4) Select all the comedic films and sort them by rental rate
5) Using one of the statements above, add a GROUP BY statement of your choice
6) Using one of the statements above, add a ORDER BY statement of your choice
"""))

' 1) Select all the actors with the first name of your choice'
if question==1:
    actor=sqlalchemy.Table("actor",metadata,autoload=True, autoload_with=engine)

    first_name=input("Which first name you want to look for? ")
    actors=sqlalchemy.select([actor]).where(actor.columns.first_name==first_name)

    response_proxy=conection.execute(actors)
    response_set=response_proxy.fetchall()
    pprint(response_set)

'2) Select all the actors and the films they have been in'
if question==2:
    film_actor=sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)
    actor=sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
    film=sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)

    join_statement=actor.join(film_actor, film_actor.columns.actor_id==actor.columns.actor_id).join(film, film_actor.columns.film_id==film.columns.film_id)
   #join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == film_actor.columns.film_id)
    query2=sqlalchemy.select([film.columns.title, actor.columns.first_name, actor.columns.last_name]).select_from(join_statement)
   #query = sqlalchemy.select([film.columns.film_id, film.columns.title,actor.columns.first_name, actor.columns.last_name]).select_from(join_statement)
    response_proxy=conection.execute(query2)
    response_set=response_proxy.fetchall()
    pprint(response_set)

'3) Select all the actors that have appeared in a category of comedy of your choice'
if question==3:
    film_actor=sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)
    actor=sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
    film=sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
    film_category=sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)
    join_statement=actor.join(film_actor, film_actor.columns.actor_id==actor.columns.actor_id).join(film, film_actor.columns.film_id==film.columns.film_id).join(film_category, film_category.columns.film_id== film.columns.film_id)
    query3=sqlalchemy.select([film.columns.title, actor.columns.first_name, actor.columns.last_name]).where(film_category.columns.category_id==5).select_from(join_statement)

    response_proxy=conection.execute(query3)
    response_set=response_proxy.fetchall()
    pprint(response_set)

'4) Select all the comedic films and sort them by rental rate'
if question==4:
    film_category=sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)
    film=sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
    join_statement=film.join(film_category, film_category.columns.film_id==film.columns.film_id)
    query4=sqlalchemy.select([film.columns.title, film.columns.rental_rate]).where(film_category.columns.category_id==5).order_by(sqlalchemy.asc(film.columns.rental_rate)).select_from(join_statement)
    response_proxy=conection.execute(query4)
    response_set=response_proxy.fetchall()
    pprint(response_set)

'5) Using one of the statements above, add a GROUP BY statement of your choice' #***pending
if question==5:
    film_category=sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)
    film=sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
    join_statement=film.join(film_category, film_category.columns.film_id==film.columns.film_id)
    query5=sqlalchemy.select([film.columns.title, film.columns.rental_rate]).where(film_category.columns.category_id==5).order_by(sqlalchemy.asc(film.columns.rental_rate)).select_from(join_statement)
    response_proxy=conection.execute(query5)
    response_set=response_proxy.fetchall()
    pprint(response_set)

'6) Using one of the statements above, add a ORDER BY statement of your choice'
if question==6:
    film_category=sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)
    film=sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)
    join_statement=film.join(film_category, film_category.columns.film_id==film.columns.film_id)
    query4=sqlalchemy.select([film.columns.title, film.columns.rental_rate]).where(film_category.columns.category_id==5).order_by(sqlalchemy.asc(film.columns.rental_rate)).select_from(join_statement)
    response_proxy=conection.execute(query4)
    response_set=response_proxy.fetchall()
    pprint(response_set)

