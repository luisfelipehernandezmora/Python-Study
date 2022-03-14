import random
from datetime import datetime

def challenge():
    permission=False
    dt = datetime.today()  # Get timezone naive now
    initial = dt.timestamp()
    print(initial)
    wait=10
    a=random.randint(5,15)
    b=random.randint(12,19)
    while True:   
        dt = datetime.today()  # Get timezone naive now
        again = dt.timestamp()
        c=int(input(f"How much is {a}*{b}? "))
        f=round(wait-(again-initial),0)
        print(f"You have {f} seconds left!")
        again = dt.timestamp()
        if again-initial > wait:
            print('You took too long!')
            permission=False
            break
        if again-initial < wait and c==a*b:
            print("got it")
            permission=True
            break
    return(permission)

a=challenge()
if a==True:
    print(f"So the you got it!")