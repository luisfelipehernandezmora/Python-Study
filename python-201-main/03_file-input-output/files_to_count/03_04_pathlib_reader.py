# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.
import os
import pathlib
from pathlib import Path
import csv
folder=pathlib.Path("C:/Users/Amma/Desktop/Coding Nomads/python-201-main/02_more-datatypes/Projects/files for the example_file counter")
types=set()
conteo=[]
cuenta=[]
dict={}
for file in folder.iterdir():
    cuenta.append(file.suffix)
    types.add(file.suffix)
for elem in types:
    conteo.append(elem)
for elem in conteo:
    dict[elem]=cuenta.count(elem)
print(dict)
path_write=pathlib.Path(r"C:\Users\Amma\Desktop\Coding Nomads\python-201-main\02_more-datatypes\Projects\files for the example_file counter\write_more_typesV2.csv")
existente=os.path.isfile(r"C:\Users\Amma\Desktop\Coding Nomads\python-201-main\02_more-datatypes\Projects\files for the example_file counter\write_more_typesV2.csv")
if existente==False:
    with open(path_write,"w") as csvfile:
        header = dict.keys()
        data=dict.values()
        countwriter = csv.writer(csvfile)
        countwriter.writerow(header)
        countwriter.writerow(data)
else:
    print("yay!")
    with open(path_write,"a") as csvfile:
        data=dict.values()
        countwriter = csv.writer(csvfile)
        countwriter.writerow(data)          