# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.
import pathlib
from pprint import pprint
folder=pathlib.Path("/home/luisfelipe/Coding Nomads/python-201-main/03_file-input-output/words.txt")
folder2=pathlib.Path("/home/luisfelipe/Coding Nomads/python-201-main/03_file-input-output/words_in_reverse.txt")

clear=[]
reverse_list=[]
with open (folder,"r") as file:
    a=file.readlines()
for elem in a:
    b=elem[:-1]
    clear.append(b)
for word in clear:
    new=word[::-1]
    reverse_list.append(new)
with open(folder2,"a") as file:
    for each in reverse_list:
        file.write(each)
        file.write("\n")
        