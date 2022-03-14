# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

class Vegetable():
    """This datatype for items in a market with two qualities.

    Args:
        1st arg: Name of the vegetable
        2nd arg: Price in the market that day 

    Returns:
        A Vegetable object with name and price.
        """
    def __init__(self, name, price):
        self.name=name
        self.price=price
    def __str__(self) -> str:
        return (f"{self.name}({self.price})")
    def __repr__(self) -> str:
        return(f"Vegetable(name={self.name}, price={self.price})")

brocoli=Vegetable("Brocoli",800)
carrots=Vegetable("carrots",650)
tomato=Vegetable("tomato",1000)
plums=Vegetable("plums",2000)
strawberry=Vegetable("strawberry",2000)

market_list=[brocoli,carrots,tomato,plums,strawberry]

for item in market_list:
    print(f"In this trip to the shop we have to buy {item.name} and it cost {item.price} CRC")
        

