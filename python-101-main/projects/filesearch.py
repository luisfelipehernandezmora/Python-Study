# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.
import pathlib
from collections import Counter
way="/home/luisfelipe/Coding Nomads/python-101-main"

#Define the path. Using way variable to able to concatanate strings downwards
folder=pathlib.Path(way)

def buscador(folder):
    """It will tell the folders and files within the path given """

    res1={}                #A dictionary to store how many of each extension the path have
    folders1=[]            #A list to store the name of the folders (since they have no extension)
    cantidades=[]          #A step into making the res dictionary
    for file in folder.iterdir():
        ext=file.suffix    #Got the extension
        if ext=="":        #find the first level of subfolders 
            name=file.stem
            folders1.append(name)
            ext="subfolder"
        cantidades.append(ext)
    for i in cantidades:
        res1[i]=cantidades.count(i)
    level1=[]
    for i in folders1:
        path=way+"/"+i      #Create each of the new paths
        level1.append(path)
    b=[res1, level1]
    return(b)

a=buscador(folder)
first_level_files=a[0]
first_level_subfolders=a[1]

second_level_files={}
second_level_files=Counter() #Counter is used to add dictionaries adding the values of the common keys
second_level_subfolders=[]

for name in first_level_subfolders:
    subfolder=pathlib.Path(name)
    second_run=buscador(subfolder)
    b=Counter(second_run[0])
    c=second_run[1]
    second_level_files+=b
    second_level_subfolders.append(c)

print(f"So you went two levels deep, the first level have this many files \n {first_level_files} \n then in those subfolders you have total these files: \n {second_level_files} and {len(second_level_subfolders)} subfolder")

