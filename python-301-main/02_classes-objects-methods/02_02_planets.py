# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    """Class of planets with basic astronomical information.

    Args:
        1st arg: Name of the planet
        2nd arg: Predominant color of the planet 
        3rd arg: Distance from the sun in Astronomical units (AU)
        4th arg: Mass expressed in Earth's mass
        5th arg: Radius in km
  
    Returns:
        A planet object with it's main features.
        """
    def __init__(self,name,color,distance_sun,mass,radius):
        self.name=name
        self.color=color
        self.distance_sun=distance_sun
        self.mass=mass
        self.radius=radius
    def __str__(self) -> str:
        return(f"Planet({self.name},{self.color},{self.distance_sun},{self.mass},{self.radius})")

earth=Planet("Earth","blue",1,1,6371)
mars=Planet("Mars","red",1.52,0.15,3396)
jupiter=Planet("Jupiter","yellow",5.2,318,71492)
saturn=Planet("Saturn","with rings",9,95,60268)

