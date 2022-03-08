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
            self.hp+=10
        else:
            self.hp+=5