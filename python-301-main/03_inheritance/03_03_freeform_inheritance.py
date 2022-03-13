# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

from cinema import *

class Dim_3(Action_movie):
    """Creates a 3d an action movie with 3d cinema rooms features"""
    def __init__(self, title, year, price, language, audio, pg=13):
        super().__init__(title, year, price, language, audio, pg)
        self.language=language
        self.audio=audio
    
    def special_sound(self):
        print(f"The special audio format and effects of your movie is {self.audio}")
    

