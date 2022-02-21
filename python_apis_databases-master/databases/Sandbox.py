'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''
# import sqlalchemy
# import os
# from pprint import pprint
# import sqlalchemy_utils


#Keep your (strong) mysql password safe 
# user=os.environ["username"]
# key=os.environ["mysql_pass"]

# engine = sqlalchemy.create_engine('mysql+pymysql://'+user+':'+key+'@localhost/GoodDB')
# conection=engine.connect()
# metadata=sqlalchemy.MetaData()

# Users=sqlalchemy.Table('Users',metadata,autoload=True,autoload_with=engine)
# a=Users.columns.keys()
# print(a, type(a))



# response_proxy=conection.execute(query)

from datetime import date
# datetime(YYYY,MM,DD)
# aries 3-21 to 4-19
aries_start = date(1, 12, 21)
aries_end = date(2, 2, 19)
birthday = date(2001, 1, 23)
if aries_end.month<aries_start.month:
    # To make 2 scenarios, one for each year
    mid1=date(1, 12, 31)
    mid2=date(2, 1, 1)
    birthday1=date(aries_start.year,birthday.month,birthday.day) #For the first part of the year
    birthday2=date(aries_end.year,birthday.month,birthday.day) #For the second part of the year
    if aries_start <= birthday1 <= mid1:
        print("You're an aries!", birthday1)
    if  mid2 <= birthday2 <= aries_end:
        print("You're an aries!", birthday2)



   
   
   
    