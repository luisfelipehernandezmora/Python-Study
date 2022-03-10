#Weapons: Sword, Dilusive talk, fist

import random

class Hero():
    """Class to define the Hero

    Args:
        1st arg: name
        2nd arg: level 
        3rd arg: stength
        4th arg: bag     
                
    Returns:
        A Hero object with:(name, level, stength, bag)
        """
    def __init__(self, name, level, strength, bag):
        self.name=name
        self.level=level
        self.strength=strength
        self.bag=bag

    def __str__(self):
        return(f"Hero(name={self.name}, level={self.level}, strength={self.strength}, bag={self.bag})")

    def attack(self,other):
        return(f"Something")

    def roll_dice(self,other):
        rand_num1=round(random.randint(1,10)*self.level/10,0)
        rand_num2=round(random.randint(1,10)*other.level/10,0)
        if rand_num1>rand_num2:
            other.strength-=self.level/10
            self.level+=1
            print(f"Well done {self.name} you won over {other.name}!")
        elif rand_num2>rand_num1:   
            self.strength-=other.level/10
            other.level+=1
            print(f"Well done {other.name} you won over {self.name}!")
        elif rand_num2==rand_num1:
            print(f"Wow good luck! you both better run!")

luke=Hero("Luke",12,10,["sword","spell"])
vader=Hero("Vader",15,9,["sword","laser"])
i=0
while luke.level<25 and vader.level<25:
    atack=luke.roll_dice(vader)
    print(atack, luke, vader,i)
    i+=1
