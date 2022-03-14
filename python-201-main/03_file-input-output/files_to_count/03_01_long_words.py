# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).
import pathlib
from pprint import pprint
folder=pathlib.Path("/home/luisfelipe/Coding Nomads/python-201-main/03_file-input-output/words.txt")
clear=[]
long=[]
with open (folder,"r") as file:
    a=file.readlines()
for elem in a:
    b=elem[:-1]
    clear.append(b)
for word in clear:
    if len(word)>20:
        long.append(word)
print(long)