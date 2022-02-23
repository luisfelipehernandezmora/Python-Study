# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

text=input("Insert a text ")
lista=text.split(sep=" ")
#print(lista)
comon={}
store=[]
for word in lista:
    number_of_times=lista.count(word)
    comon[word]=number_of_times
maxi=max(comon.values())
#print(maxi)  
most_common=comon.items()
print(most_common)
for key in comon.keys():
    if comon[key]==maxi:
        store.append(key)
print(f"The words that more appear in the text are {store} and appear {maxi} times")
    
