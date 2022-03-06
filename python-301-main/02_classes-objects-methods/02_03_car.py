# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.
class Car():
    """Class of cars with basic mechanical information.

    Args:
        1st arg: model
        2nd arg: year 
        3rd arg: Max Speed in km/h
          
    Returns:
        A car object with it's main features.
        """
    def __init__(self,model,year,max_speed):
        self.model=model
        self.year=year
        self.max_speed=max_speed
    def increase_speed(self):
        self.max_speed+=5

beetle=Car("volkswagen beetle",1970,100)

modern=beetle.increase_speed()
print(f"{modern.max_speed}")
