# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages
import random


def is_div(num):
    desicion=False
    if num%4==0:
        desicion=True
    elif num%7==0:
        desicion=True
    else:
        desicion=False
    return(desicion)
#num=int(input("Introduce a number to see if it is divisible by 4 or 7 "))
num=random.randint(0,10000000)
result=is_div(num)
print(f"So the number is {num} and is {result} divisible by 4 or 7")