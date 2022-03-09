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

    def __str__():
        return(f"Hero(name={self.name}, level={self.level}, strength={self.strength}, bag={self.bag})")

    def attack(self,other):
        return(f"Something")

    def roll_dice(self,other):
        rand_num=random.randint(1,6)
        




class Opponent()