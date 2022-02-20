# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.
# Hard-code a word that needs to be guessed in the script
# Print an explanation to the user
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it
import pathlib
import random
from pprint import pprint
import requests
path=pathlib.Path("/home/luisfelipe/Coding Nomads/python-101-main/projects/English_words.txt")
with open (path) as file:
    a=file.readlines()
score=10
c=[]
mystery=[]              #Box where the word will be constructed on different attempts
bank_of_letters=set()   #In this box it will be veryfied if the attempts match the guess
for word in a:
    if word=="yourself":
        c.append(word)
        continue
    elif word=="a\n":
        continue
    b=word[:-1]
    c.append(b)
guess=random.choice(c)
guess_hecho_lista=list(guess)
largo=len(guess)        #find out how many letters have the guess
for i in range(len(guess)):
    mystery.append("_")
    i=+1
for char in guess:
    bank_of_letters.add(char)
def list_to_str(list):
    mystery_to_show=" ".join(list)
    return(mystery_to_show)
def translate(word):
    url="https://dictionaryapi.com/api/v3/references/spanish/json/"+word+"?key=fe594801-4f52-4e7d-9340-4317a163897a"
    response=requests.get(url).json()[0]
    definition=response["shortdef"]
    stem=response["meta"]["stems"]
    meaning=(f"El significado de la palabra {word} es: {definition}")
    stem_ans=(f"{word} también tiene palabras derivadas como: {stem}, Estas se pueden usar en un monton de contextos, anotalas y practique oraciones en las que las puede utilizar!")
    return(meaning,stem_ans)
intentadas=[]
cuantas_veces=int()
while score>0:          #Keep the player limited in tries
    indexes=[]
    tri=input(f"Guess a letter you still have {score} points available, so far you have tried {intentadas} ")
    intentadas.append(tri)
    if tri in bank_of_letters:
        for i in range(len(guess_hecho_lista)):
            if guess_hecho_lista[i]==tri:
                indexes.append(i)
        for x in indexes:
            mystery[x]=tri
            step_show=list_to_str(mystery)
            print(f"Good job! So far you have discovered: {step_show} ")
            if "_" not in mystery:
                print(f"And congrtulations! Now you have won! with {score} attempts still possible")
                look=translate(guess)
                meaning=look[0]
                stem_ans=look[1]
                print(meaning)
                print(stem_ans)
                quit()
    else:
        score-=1
        print(f"The letter is not in the word! You have {score} attempts left!")
        # *** **** **** Here is where I want to include an image with Pillow, of the drawing of 
        # Hangman game drawing step by step as the player plays. But not yet acomplished 
print(f"Oh you lost, sorry. You need to guess in less attempts")     


    