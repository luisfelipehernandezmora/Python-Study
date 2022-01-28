# Use the modulo operator to confirm which of the values
# shown below are divisible by seven.

num_1 = 42
num_2 = 137
num_3 = 455
num_4 = 1997
list1=[num_1,num_2,num_3,num_4]
x=0
for x in list1:
    if x%7==0:
        print(x,"Is divisible by 7! Yay")
    else:
        print(x,"Is not divisible by 7! what to do?")
    x+=1

    