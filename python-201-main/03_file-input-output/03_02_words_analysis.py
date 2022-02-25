# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.
import pathlib
folder=pathlib.Path("/home/luisfelipe/Coding Nomads/python-201-main/03_file-input-output/words.txt")
clear=[]
with open (folder,"r") as file:
    a=file.readlines()
for elem in a:
    b=elem[:-1]
    clear.append(b)
total=len(clear)
temp=[]
for word in clear:
    temp.append(len(word))
minimun=min(temp)
maximum=max(temp)
mini=[]
maxi=[]
for word in clear:
    if len(word)==minimun:
        mini.append(word)
    elif len(word)==maximum:
        maxi.append(word)
print(f"The shortest words are {mini} and the  longest are {maxi} and there is a total of {total} words in the {folder} document")
