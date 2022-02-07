'''
Using the Chuck Norris API in combination with the datamuse API
( https://api.chucknorris.io/ - https://www.datamuse.com/api/ )

* Query the chucknorris api for a sentence
* Use the last word of that sentence to send a query to the Datamuse API
  and use the rel_rhy (or rel_nry) query parameter to fetch a word that rhymes
* Repeat a coupe of times and store the sentences and rhyme words
* Synthesize the collected results into an avant-garde poem and post on the forum ;)

'''
import requests
from pprint import pprint

#Get a random Chuck Norris phrase
url="https://api.chucknorris.io/jokes/random"
frase=requests.get(url).json()["value"]

# Get the last word of the sentence to look a rhyme to it
lista=[]
#print(type(frase))
lista=frase.split()

#Take that last word
last_word=lista[-1]
#take awaya the dot of the word, to avoid problems with the rhyme api
last_word=last_word[:-1]
rima="https://api.datamuse.com/words?rel_rhy="+last_word
rimas=requests.get(rima).json()[0]["word"]

ful=frase+" "+rimas
print(ful)

#Write in the .txt file
with open ("Chuck_Norris_Poem.txt","a") as file:
    file.write(ful + "\n")
    
    