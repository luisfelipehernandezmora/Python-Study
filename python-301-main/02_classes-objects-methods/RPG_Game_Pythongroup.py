#Weapons: Sword, Dilusive talk, fist
import random
import time
from datetime import datetime
secs=3

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

class Hero():
    """Class to define the Hero

    Args:
        1st arg: name
        2nd arg: level 
        3rd arg: stength
        4th arg: bag
        5th arg: active (True)     
                
    Returns:
        A Hero object with:(name, level, stength, bag, active)
        """
    def __init__(self, name, level, strength, bag, active):
        self.name=name
        self.level=level
        self.strength=strength
        self.bag=bag
        self.active=active

    def __str__(self):
        return(f"Hero(name={self.name}, level={self.level}, strength={self.strength}, bag={self.bag}, active={self.active})")

    def run_away(self,other):
        print(f"So you want to run? Only if you guess correctly the math operation you can proceed")     
        d=challenge()               
        if d==False:
            print(f"Oh You run out of time, you have to be sharper and quicker, so you have to figth!")
            self.attack(other)
        elif d:
            print(f"Oh right! at least you are studying, ok fine, go!")
        return(None)

    def attack(self,other):
        rand_num1=round(random.randint(1,10)*self.level/10,0)
        rand_num2=round(random.randint(1,10)*other.level/10,0)
        if rand_num1>rand_num2:
            other.active=False
            self.level+=1
            print(f"Well done {self.name} you won over {other.name},\n the enemy have become inactive from the game!")
        elif rand_num2>rand_num1:   
            self.strength-=other.level/10
            other.level+=1
            if self.strength<=0:
                print(f"Oh {self.name} you have lost the game")
                quit()
            print(f"Well done {other.name} you won over {self.name}! and now {self.name} have to wait for {secs} seconds")
            time.sleep(secs)
        elif rand_num2==rand_num1:
            print(f"Wow good luck! you both better run!")

class Opponent():
    """Class to define the Opponent

    Args:
        1st arg: name
        2nd arg: level 
        3rd arg: stength
        4th arg: bag
        5th arg: active (True to begin, but when defeat on combat becomes False and is leave outside of combat)     
                
    Returns:
        A Opponent object with:(name, level, stength, bag, active)
        """
    def __init__(self, name, level, strength, bag, active):
        self.name=name
        self.level=level
        self.strength=strength
        self.bag=bag
        self.active=active

    def __str__(self):
        return(f"Opponent(name={self.name}, level={self.level}, strength={self.strength}, bag={self.bag}, active={self.active})")

luke=Hero("Luke",12,10,["sword","spell"],True)
vader=Opponent("Vader",15,9,["sword","laser"],True)

#luke.run_away(vader)
luke.attack(vader)
