# Write your guess-the-number game again from scratch to revisit the concepts you learned.
# Change the game's functionality so a user has only a limited number of tries to guess the right number. Which loop will you use for this implementation?
# Write a guess-the-word program. Provide some hints to make it easier.

import random

a=0
b=25
guess=None
num=random.randint(a,b)
print(num)
tries=int(input("How many tries you want for this game? "))

while guess!=num:
    guess=int(input(f"Guess a number between {a} and {b} ")) 
    if guess==num:
        break
    tries-=1
    print(f"You have {tries} tries left")  
    if tries==0:
        print("I am sorry, you need more tries or more luck next time ;) ")
        quit()   

print(f"Hey you go it! Your guess of {guess} and the secret number {num} are equal! ")