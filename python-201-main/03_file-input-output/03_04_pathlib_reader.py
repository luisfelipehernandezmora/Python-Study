# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.
import os
import pathlib
import csv
folder=pathlib.Path("/home/luisfelipe/Coding Nomads/python-201-main/03_file-input-output/files_to_count")
types=set()
conteo=[]
cuenta=[]
dict={}
for file in folder.iterdir():
    cuenta.append(file.suffix)
    types.add(file.suffix)
conteo=list(types)
for elem in conteo:
    dict[elem]=cuenta.count(elem)
print(dict)
path_write=pathlib.Path("/home/luisfelipe/Coding Nomads/python-201-main/03_file-input-output/summary_types.csv")
existente=os.path.isfile("/home/luisfelipe/Coding Nomads/python-201-main/03_file-input-output/summary_types.csv")
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