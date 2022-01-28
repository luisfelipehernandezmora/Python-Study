# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
import random
a=0
b=10
num=random.randint(a,b)
print(num)
guess=None
c=int(input("How many tries you want for this round? "))
while guess!=num:
    guess=int(input(f"Guess a number, you have only {c} more attempts "))
    if guess==num:
        print(f"Hey you found that the secret number is {num}! Congrats!")
        break
    c-=1
    if c<1:
        print("Oh sorry, it was your last try, better luck next time!")
        quit()