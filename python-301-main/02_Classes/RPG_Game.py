#Weapons: Sword, Dilusive talk, fist

import random
import time
secs=3
def count_down():
    i=10
    while i>0:
        print(f"You still have {i} seconds left to think")
        time.sleep(1)
        i-=1
    return(False)

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
        a=random.randint(5,15)
        b=random.randint(12,19)
        d=count_down()
        c=int(input(f"What is the result of {a}x{b}? "))
        #d=count_down()

        if d==False:
            print(f"Oh You run out of time, you have to be sharper and quicker")
        if a*b==c:
            print(f"Oh right! at least you are studying, ok fine, go!")

        else:
            print(f"I am sorry but {a}x{b} is not {c}, you will have to attack")
            self.attack(other)
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

luke.run_away(vader)






# i=0
# while luke.level<25 and vader.level<25:
#     atack=luke.attack(vader)
#     print(atack, luke, vader,i)
#     i+=1
