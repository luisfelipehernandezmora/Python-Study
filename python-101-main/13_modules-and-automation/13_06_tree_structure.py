# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

#select which folder you want to walk through
#Display all the files in that folder, make the posibility to open a folder inside
#show all the files inside, 
#Select and print the one wo .py

import pathlib

folder=pathlib.Path("C:/Users/Amma/Desktop/Coding Nomads/python-101-main")
for file in folder.iterdir():
    print(file.name)
    if file.is_dir():
        for file2 in file.iterdir():
            if file2.suffix==".py":
                print(file2)