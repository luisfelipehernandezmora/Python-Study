# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`
import random
class Pokemon:
    """Class to create Pokemons

    Args:
        1st arg: name
        2nd arg: Type (water, fire or grass!) 
                     
    Returns:
    A list of information of the country in order: [name, veg/non veg, calories, price]
    """ 
    def __init__(self, name, type, hp, max_hp):
        self.name=name
        self.type=type
        self.hp=hp
        self.max_hp=max_hp
    
    def __str__(self) -> str:
        return(f"Pokemon(name = {self.name}, Type = {self.type}, hp = {self.hp}, max_hp = {self.max_hp})")
    
    def feed(self):
        if self.hp<self.max_hp/2 :
            self.hp+=self.max_hp*0.1
        else:
            self.hp+=self.max_hp*0.05
        if self.hp>=self.max_hp:
            self.hp=self.max_hp
        return(f"Good meal! Your current hp is {self.hp}/{self.max_hp}")
        
    def attack(self,other):
        damage=self.max_hp*0.1*random.randrange(1,4)
        if self.type=="water" and other.type=="fire":
            real_damage=damage*1.2
        elif self.type=="water" and other.type=="grass":
            real_damage=damage*0.8
        elif self.type=="water" and other.type=="water":
            real_damage=damage
        elif self.type=="fire" and other.type=="fire":
            real_damage=damage
        elif self.type=="fire" and other.type=="grass":
            real_damage=damage*1.2
        elif self.type=="fire" and other.type=="water":
            real_damage=damage*0.8
        elif self.type=="grass" and other.type=="fire":
            real_damage=damage*0.8
        elif self.type=="grass" and other.type=="grass":
            real_damage=damage
        elif self.type=="grass" and other.type=="water":
            real_damage=damage*1.2
        other.hp-=real_damage
        print(f"{self.name} attacking with: {real_damage}")
        return(real_damage)
    def battle(self,other):
        i=1
        while self.hp>0 and other.hp>0:
            if i%2==0:
                self.attack(other)
            else:
                other.attack(self)
            print(self.name,self.hp)
            print(other.name,other.hp,"\n")
            i+=1
        if self.hp<=0:
            other.max_hp+=2
            other.hp+=4
            msj=f"Excellent {other.name}! you won the battle and you receive some health booster \n New health {other.hp} and New health max {other.max_hp} keep rocking!"
        elif other.hp<=0:
            self.max_hp+=2
            self.hp+=4
            msj=f"Excellent {self.name}! you won the battle and you receive some health booster \n New health {self.hp} and New health max {self.max_hp} keep rocking!"
        return(msj)

Bulbasur=Pokemon("Bulbasur", "grass", 25, 25)
Flareon=Pokemon("Flareon", "fire", 25, 25)
Squirtle=Pokemon("Squirtle", "water", 25, 25)

a=Squirtle.battle(Flareon)
print(a,Squirtle,Flareon)