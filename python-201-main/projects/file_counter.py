# Add the code for the file counter script that you wrote in the course.
from itertools import count
import pathlib
import csv
#  \\wsl$\Ubuntu-20.04\home\luisfelipe\Coding Nomads\python-201-main\projects
folder=pathlib.Path("/home/luisfelipe/Coding Nomads/python-201-main/projects")
extensiones=[]
cantidades=dict()
for file in folder.iterdir():
        file_name=file.name
        c=file_name.split(".") 
        ext="."+c[-1]
        #print(c,ext) 
        extensiones.append(ext)
print(extensiones)
for elem in extensiones:
        cantidades[elem]=extensiones.count(elem)
print(cantidades)

for key in cantidades.keys():
        data = [key,cantidades[key]]
        with open ("file_counter.csv","a") as file:
                writer = csv.writer(file)
                writer.writerow(data)
