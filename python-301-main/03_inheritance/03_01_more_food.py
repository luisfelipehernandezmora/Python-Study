# Create another child class that inherits from `Ingredient()`. You can use
# the code you wrote yourself, or continue working with the one provided below.
# Implement at least one extra method for your child class, and override the
# `expire()` method from the parent `Ingredient()` class.
class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."


class Spice(Ingredient):
    """Models a spice to flavor your food."""

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")

class Bread(Ingredient):
    """A Method to define Bread types and their cares for cooking

    Args:
        1st arg: Name of the bread
        2nd arg: Amount available
        3rd arg: Minutes in the oven
        4th arg: Gluten free or not

    Returns:
        A Vegetable object with name and price.
        """
    def __init__(self, name, amount, oven, gluten_free):
        super().__init__(name, amount)
        self.oven=oven
        self.gluten_free=gluten_free

    def expire(self):
        print(f"Smeel your {self.name} it might be getting moldy \n")
        self.name="moldy"+self.name

    def bake(self,):
        if self.gluten_free==True:
            print(f"Your {self.name} gluten free bread needs {self.oven} minutes to be baked")
        else:
            print(f"Your {self.name} bread needs {self.oven} minutes to be baked. And beware, it have gluten!")


if __name__ == '__main__':
    centeno=Bread("Centeno", 5, 12, False)
    normal=Bread("Baguete", 5, 10, False)
    brown=Bread("Brown bread", 5, 7, True)

    breads=[centeno,normal, brown]
    for i in breads:
        i.bake()
        i.expire()
    
