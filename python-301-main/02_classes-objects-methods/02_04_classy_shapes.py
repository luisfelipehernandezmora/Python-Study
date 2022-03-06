# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.
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
        area=self.length*self.width
        perimeter=2*(self.length+self.width)
        return(f"The area of the rectangle is {area} \n and the perimeter is {perimeter}")

rectangulo=Rectangle(15,10).basic_geometry()
print(rectangulo)

        
