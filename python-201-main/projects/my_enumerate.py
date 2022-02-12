# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(list): 
      n=len(list)
      new=[]
      for i in range(n):
            temp=()
            temp=i,list[i]
            new.append(temp)          
      return(new)

lista=["uno","dos","tres","cuatro","cinco","seis","siete","ocho"]

c=my_enumerate(lista)
print(c,"own function")

d=enumerate(lista,start=0)
for i in d:
      print(i)