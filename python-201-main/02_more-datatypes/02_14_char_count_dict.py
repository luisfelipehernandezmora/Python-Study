# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur.biFor example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}
abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
text=input("insert a text to count the letters ")
#text="Sequoia Capital is an American venture capital firm. The firm is headquartered in Menlo Park, California and mainly focuses on the technology industry. It was the Top VC fund company in 2019."
lista=text.split(" ")
dict={}
big_list=[]
print(lista)
if len(lista)>1:
    for word in lista:
        temp=list(word)
        big_list.extend(temp)
    for char in big_list:
        dict[char]=big_list.count(char)
else:
    lista2=list(lista[0])
    for char in lista2:
        dict[char]=lista2.count(char)
print(dict)


    