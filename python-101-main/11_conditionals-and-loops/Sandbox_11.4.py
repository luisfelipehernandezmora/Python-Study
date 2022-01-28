#for i in range(5):
    #for char in "hello":
        #print(i, char)

import string
import random
word=str(input("Write a text you want to cypher: "))
new="".join(random.choice(string.ascii_lowercase) for x in range(len(word)))
print(new)

import string
import random
newword = ''
word = input("type a new word: ")
for char in word:
    for char in random.choice(string.ascii_lowercase):
        newword += char
print(newword)
