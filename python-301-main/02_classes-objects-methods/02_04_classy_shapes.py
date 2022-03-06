# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.
import math
from turtle import circle


class Rectangle():
    """Class to define a rectangle.

    Args:
        1st arg: length in the desired metric unit
        2nd arg: width in the desired metric unit
        
    Returns:
        The area in square (metric unit) and the perimeter in metric unit.
        """
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def __str__(self) -> str:
        return(f"A rectangle to be defined by length and width")
    def basic_geometry (self):
        area=round(self.length*self.width,2)
        perimeter=round(2*(self.length+self.width),2)
        return(f"The area of the rectangle is {area} \n and the perimeter is {perimeter}")

class Circle():
    """Class to define a circle.

    Args:
        1st arg: radius in the desired metric unit
                
    Returns:
        The area in square (metric unit) and the circunference in metric unit.
        """
    def __init__(self,radius):
        self.radius=radius
    def __str__(self) -> str:
        return(f"A circle to be defined by it's radius")
    def basic_geometry(self):
        area=round(math.pi*(self.radius)**2,2) 
        perimeter=round(2*math.pi*self.radius,2)
        return(f"The area of the circle is {area} \n and the circunference is {perimeter}")

rectangulo=Rectangle(15,10).basic_geometry()
circulo=Circle(4).basic_geometry()
print("\n",rectangulo,"\n")
print(circulo)


        
