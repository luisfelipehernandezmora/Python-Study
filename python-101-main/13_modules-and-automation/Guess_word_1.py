# Write your guess-the-number game again from scratch to revisit the concepts you learned.
# Change the game's functionality so a user has only a limited number of tries to guess the right number. Which loop will you use for this implementation?
# Write a guess-the-word program. Provide some hints to make it easier.

from ctypes import POINTER


guess=str()
secret="apple"

tries=int(input("How many tries you want for this game? "))
hint1=len(secret)
hint2=secret[0]
hint3=secret[-1]
rounds=0
print("""So this is the game, you have to guess a word and you have 3 hints 
only, be careful when to use them and you have to uncover some letters 
to use all the hints. You have to type 'Yes' in order to use the help""")
# help=input("You want some hint?")
while tries>0:
    guess=input("Guess which is the secret word ").lower()
    if guess==secret:
        print(f"Hey you got it! the secret word is {guess}")
        quit()
    tries-=1
    if tries==0:
        print("Oh you exceed the amount of attempts, play again!")
        quit()
    rounds+=1
    print(f"You have {tries} tries left") 
    if rounds==3:
        ask1=input("You want some help? ")
        if ask1=="Yes":
            print(f"The lenght of the word is {hint1}")
    if rounds==5:
        ask1=input("You want some help? ")
        if ask1=="Yes":
            print(f"The lenght of the word is {hint1}")  
            ask2=input("You want some more help? ")
            if ask2=="Yes":
                print(f"The first character of the word is {hint2}")
    if rounds>6:
            ask1=input("You want some help? ")
            if ask1=="Yes":
                print(f"The lenght of the word is {hint1}")  
                ask2=input("You want some more help? ")
                if ask2=="Yes":
                    print(f"The first character of the word is {hint2}")   
                    ask3=input("You want even more help? ")
                    if ask3=="Yes":
                        print(f"The last character of the word is {hint3}")        
     
