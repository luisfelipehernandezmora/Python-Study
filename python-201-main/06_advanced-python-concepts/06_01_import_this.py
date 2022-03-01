# Add the necessary import statement in order to make this script
# produce output. Don't change any of the existing code.
# All the necessary variables and functions are
# already defined in the `codingnomads/` folder.

#from codingnomads.recipes import soup  #Way1
#import codingnomads.recipes.soup        #Way2
from codingnomads.recipes.soup import make_soup   #Way3

#sopa = soup.make_soup("potato")        #Way1
#sopa = codingnomads.recipes.soup.make_soup("potato") #Way2
sopa = make_soup("potato")        #Way3

print(sopa)
