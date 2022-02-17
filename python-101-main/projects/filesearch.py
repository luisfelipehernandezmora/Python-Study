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
way="/home/luisfelipe/Coding Nomads/python-101-main/projects/filesearch_task"
folder=pathlib.Path(way)

def buscador(folder):
    res1={}
    folders1=[]
    cantidades=[]
    for file in folder.iterdir():
        ext=file.suffix
        cantidades.append(ext)
        #find the first level of subfolders 
        if ext=="":
            name=file.stem
            folders1.append(name)
    for i in cantidades:
        res1[i]=cantidades.count(i)
    level1=[]
    for i in folders1:
        path=way+"/"+i
        level1.append(path)
    b=[res1, level1]
    return(b)

a=buscador(folder)
first_level_files=a[0]
first_level_subfolders=a[1]

second_level_files={}
second_level_subfolders=[]

for subfolder in first_level_subfolders:
    second_run=buscador(subfolder)
    b=second_run[0]
    c=second_run[1]
    second_level_files+=b
    second_level_subfolders.append(c)


