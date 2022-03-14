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
