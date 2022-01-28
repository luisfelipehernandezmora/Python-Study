# Write your guess-the-number game again from scratch to revisit the concepts you learned.
# Change the game's functionality so a user has only a limited number of tries to guess the right number. Which loop will you use for this implementation?
# Write a guess-the-word program. Provide some hints to make it easier.

import random

a=0
b=25
guess=None
num=random.randint(a,b)
print(num)

while guess!=num:
    guess=int(input(f"Guess a number between {a} and {b} "))       

print(f"Hey you go it! Your guess of {guess} and the secret number 25 {num} are equal! ")
