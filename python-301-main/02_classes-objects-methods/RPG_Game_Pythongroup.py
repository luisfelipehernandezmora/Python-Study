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

    def check(self):
        print(f"Your actual status is {self}")

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
figther1=Opponent("Jack",10,9,["sword"],True)
fighter2=Opponent("Red sea",9,9,["sword"],True)
fighter3=Opponent("Star Fish",11,9,["sword"],True)
fighter4=Opponent("Death star",12,9,["sword"],True)
oponentes=[vader,figther1, fighter2, fighter3, fighter4]

# print(len(oponentes))
while len(oponentes)>0:
    ask=input(f"{luke.name} You want to walk front, left or rigth? or you want to check your health? (check) ")
    if ask=="front":
        destiny=random.randint(1,2)

        if destiny ==1:
            ask2=input(f"Oh, you found an Opponent, you want to attack or run away? ")
            current_enemy=random.choice(oponentes)
            if ask2=="attack":
                luke.attack(current_enemy)
                if current_enemy.active==False:
                    oponentes.remove(current_enemy)
                    print(f"{len(oponentes)} left in the field")
                continue
            elif ask2=="run away":
                luke.run_away(current_enemy)
                if current_enemy.active==False:
                    oponentes.remove(current_enemy)
                    print(f"{len(oponentes)} left in the field")
                continue
        if destiny ==2:
            print(f"Good news, the path is free for now, keep exploring")
            continue

    elif ask=="left":
        destiny=random.randint(1,2)

        if destiny ==1:
            ask2=input(f"Oh, you found an Opponent, you want to attack or run away? ")
            current_enemy=random.choice(oponentes)
            if ask2=="attack":
                luke.attack(current_enemy)
                if current_enemy.active==False:
                    oponentes.remove(current_enemy)
                    print(f"{len(oponentes)} left in the field")
                continue
            elif ask2=="run away":
                luke.run_away(current_enemy)
                if current_enemy.active==False:
                    oponentes.remove(current_enemy)
                    print(f"{len(oponentes)} left in the field")
                continue
        if destiny ==2:
            print(f"Good news, the path is free for now, keep exploring")
            continue

    elif ask=="rigth":
        destiny=random.randint(1,2)

        if destiny ==1:
            ask2=input(f"Oh, you found an Opponent, you want to attack or run away? ")
            current_enemy=random.choice(oponentes)
            if ask2=="attack":
                luke.attack(current_enemy)
                if current_enemy.active==False:
                    oponentes.remove(current_enemy)
                    print(f"{len(oponentes)} left in the field")
                continue
            elif ask2=="run away":
                luke.run_away(current_enemy)
                if current_enemy.active==False:
                    oponentes.remove(current_enemy)
                    print(f"{len(oponentes)} left in the field")
                continue
        if destiny ==2:
            print(f"Good news, the path is free for now, keep exploring")
            continue
    elif ask=="check":
        luke.check()    
print(f"Wow can't believe it, you really made it trough, congrats! You won")

