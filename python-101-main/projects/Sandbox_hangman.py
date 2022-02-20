from pprint import pprint
import requests
#word=input("Insert a word ")

def translate(word):
    #word=str
    url="https://dictionaryapi.com/api/v3/references/spanish/json/"+word+"?key=fe594801-4f52-4e7d-9340-4317a163897a"
    response=requests.get(url).json()[0]
    definition=response["shortdef"]
    stem=response["meta"]["stems"]
    meaning=(f"El significado de la palabra {word} es: {definition}")
    stem_ans=(f"{word} también tiene palabras derivadas como: {stem}, Estas se pueden usar en un monton de contextos, anotalas y practique oraciones en las que las puede utilizar!")
    return(meaning,stem_ans)
a=translate("car")
b=a[0]
c=a[1]
c