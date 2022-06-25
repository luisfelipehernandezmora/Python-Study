import json
from pprint import pprint
import os
import requests

## Creates a class for movie objects, so is easy to search by features such as director, name, etc...
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

movies_file=os.getcwd()+"/python-301-main/04_web-scraping/films.json" #give independence of the system where you run it

## Download the movies into a json if it haven't been done
if os.path.isfile(movies_file)==False:
    print(f"Oh you haven't download the movies, let's get the json!")
    response = requests.get("https://ghibliapi.herokuapp.com/films").json()
    with open(movies_file,"w") as file:
        json.dump(response,file)

## Read the file
with open (movies_file,"r") as file:
    data=json.load(file)

#Creates a list of Movie objects which have the 5 atributes title, director, dur, orig name and date
list_of_movies=[]
for elem in data:
    title=elem["title"]
    director=elem["director"]
    duration=elem["running_time"]
    original_name=elem["original_title"]
    date=elem["release_date"]
    list_of_movies.append(Movie(title,director,duration,original_name,date))
    
duration_of_movies=[]
for movie in list_of_movies: #Find the longest movie
    duration_of_movies.append(int(movie.duration))

long_movie=max(duration_of_movies)
pos=duration_of_movies.index(long_movie)
title_long=list_of_movies[pos].name
orig_long=list_of_movies[pos].original_name
print(f"\nThe longest movie lasts {long_movie} minutes and it's title is {title_long} and actually it's original name was {orig_long}\n\n\n")
print(f"And you also want all the names of titles and directors right?\n.\n.\n.")

for each in list_of_movies:     
    dir=each.director
    tit=each.name
    print(f"The movie {tit} was made by {dir}")
