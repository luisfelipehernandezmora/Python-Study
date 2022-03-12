# CLASSES AND INHERITANCE
# =======================
# 1) Define an empty `Movie()` class.
# 2) Add a dunder init method that takes two arguments `year` and `title`
# 3) Create a sub-class called `RomCom()` that inherits from the `Movie()` class
# 4) Create another sub-class of the `Movie()` class called `ActionMovie()`
#     that overwrites the dunder init method of `Movie()` and adds another
#     instance variable called `pg` that is set by default to the number `13`.
# 5) Practice planning out and flushing out these classes even more.
#     Take notes in your notebook. What other attributes could a `Movie()` class
#     contain? What methods? What should the child classes inherit as-is or overwrite?

class Movie:
    """A class that define movies with their year and title

    Args:
        1st arg: Title of the movie
        2nd arg: Year
       
    Returns:
        A Movie object with name and year.
        """

    def __init__(self, title, year, price):
        self.title=title
        self.year=year
        self.price=price

    def __str__(self) -> str:
        return(f"{self.title}({self.year})")

    def __repr__(self) -> str:
        return(f"Movie(title={self.title}, year={self.year})")
    
    def rent(self):
        """Returns rent price"""
        return(self.price)

class RomCom(Movie):
    """Defines a movie from the Romance/Comedy category"""

    def __init__(self, title, year, price):
        super().__init__(title, year, price)
        print(f"{self.title} is a movie from the Romantic/Comedy gender from the year {self.year}")
    
class Action_movie(Movie):
    """Defines an Action movie! """

    def __init__(self, title, year, price, pg=13):
        super().__init__(title, year, price)
        self.pg=pg
        print(self.pg)

if __name__=="__main__":
    a=RomCom("test movie", 2001, 2.3)
    print(a.rent())
    Batman=Action_movie("Batman", 2001, 2)