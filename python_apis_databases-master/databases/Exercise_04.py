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
# if not sqlalchemy_utils.database_exists(engine.url):
#     sqlalchemy_utils.create_database(engine.url)
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
'1) Create a table'
if question ==1:
    name=input("So, What is gonna be the name of your table? ")
    cols_names=[]
    for i in range(5):
        name_col=input(f"Write the name of the 5 columns. Use the first column for Identification of data ")
        cols_names.append(name_col)
        i+=1
        """
        """
    query=sqlalchemy.Table(name, metadata, 
        sqlalchemy.Column(cols_names[i],sqlalchemy.Integer()),
        sqlalchemy.Column(cols_names[1],sqlalchemy.String(255)),
        sqlalchemy.Column(cols_names[2],sqlalchemy.String(255)),
        sqlalchemy.Column(cols_names[3],sqlalchemy.String(255)),
        sqlalchemy.Column(cols_names[4],sqlalchemy.String(255)),

      """  sqlalchemy.Column(cols_names[0],sqlalchemy.Integer()), sqlalchemy.Column(cols_names[1],sqlalchemy.String(255)), sqlalchemy.Column(cols_names[2],sqlalchemy.String(255)),
        sqlalchemy.Column(cols_names[3],sqlalchemy.String(255)),
        sqlalchemy.Column(cols_names[4],sqlalchemy.String(255)),"""
    )
    metadata.create_all(engine)
'2) Insert data to a table'
if question ==2:
    in_table=input("In which table you want to insert data? ")
    
    # Users=sqlalchemy.Table('Users',metadata,autoload=True,autoload_with=engine)
    # a=Users.columns.keys()
    use_table=sqlalchemy.Table(in_table,metadata,autoload=True,autoload_with=engine)
    columnas=use_table.columns.keys()
    print(columnas)
    insertion=[]
    for i in range(len(columnas)):
        ask=input(f"What value you want to insert for the column {columnas[i]}? ")
        insertion.append(ask)
        i+=1
    query=sqlalchemy.insert(use_table).values(Id=insertion[0],Name=insertion[1],Email=insertion[2],Phone=insertion[3],City=insertion[4])
    #query=sqlalchemy.insert(use_table).values(columnas[0]==insertion[0],columnas[1]==insertion[1],columnas[2]==insertion[2],columnas[3]==insertion[3],columnas[4]==insertion[4])
    result_proxy=conection.execute(query)
'3) Update data in a table'
if question ==3:
    in_table=input("In which table you want to update data? ")
    use_table=sqlalchemy.Table(in_table,metadata,autoload=True,autoload_with=engine)
    columnas=use_table.columns.keys()
    column_to_update=input("Which column you want to update? ")
    new_value=input("Type your update ")
    modified_id=input("which ID is the one to update? ")
    query=sqlalchemy.update(use_table).values(Name=new_value).where(use_table.columns.Id==modified_id)
    result_proxy = conection.execute(query)

'4) Select data from a table'
if question ==4:
    in_table=input("In which table you want to select data from? ")
    use_table=sqlalchemy.Table(in_table,metadata,autoload=True,autoload_with=engine)
    columnas=use_table.columns.keys()
    select_id=input("which ID is the one to select? ")
    query=sqlalchemy.select([use_table]).where(use_table.columns.Id==select_id)
    result_proxy = conection.execute(query)
    result_set=result_proxy.fetchall()
    print(result_set)

'5) Delete data from a table'
if question ==5:
    in_table=input("In which table you want to delete data from? ")
    use_table=sqlalchemy.Table(in_table,metadata,autoload=True,autoload_with=engine)
    columnas=use_table.columns.keys()
    delete_id=input("which ID is the one to select? ")
    query=sqlalchemy.delete([use_table]).where(use_table.columns.Id==delete_id)
    result_proxy = conection.execute(query)

'6) Use at least one join in a select query ##Think how to rename this lines'
#if question ==6: