# Write a code snippet that gives a name to a `sheep`
# and uses a boolean value to define whether it has `wool` or not.
import random

n = random.randint(20,100)
print(n)
x=0
name=""
while x<n:
    letter=random.choice("wolae")
    print(letter)
    name+=letter
    x+=1
print(name)
if "wool" in name:
    print("This sheep has wool! goo for it!")
else:
    print("Not wool yet!")    
