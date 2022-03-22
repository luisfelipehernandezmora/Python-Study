import json
from pprint import pprint

class Movie:
    """Create Movie object with some information for analysis"""
    def __init__(self,name,director,duration,original_name,date):
        self.name=name
        self.director=director
        self.duration=duration
        self.original_name=original_name
        self.date=date

    def __str__(self) -> str:
        return(f"Name={self.name}, director={self.director}, duration={self.duration}, original name={self.original_name}, release date={self.date}")

folder="/home/luisfelipe/Coding Nomads/python-301-main/04_web-scraping/films.json"

with open (folder,"r") as file:
    data=json.load(file)
list_of_movies=[]
for elem in data:
    title=elem["title"]
    director=elem["director"]
    duration=elem["running_time"]
    original_name=elem["original_title"]
    date=elem["release_date"]
    list_of_movies.append(Movie(title,director,duration,original_name,date))
    
longest=[]
for movie in list_of_movies: #Find the longest movie
    print(movie)
    longest.append(int(movie.duration))

long_movie=max(longest)
pos=longest.index(long_movie)
title_long=list_of_movies[pos].name
orig_long=list_of_movies[pos].original_name
print(f"\nThe longest movie lasts {long_movie} minutes and it's title is {title_long} and actually it's original name was {orig_long}")