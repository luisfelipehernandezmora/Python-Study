# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

from statistics import mean
import random
top=random.randint(10,500)
lista=[]

for num in range(0,top):
  num=num*random.randint(0,10)+random.randint(1,5)
  if num not in lista:
    lista.append(num)
  
def stats(lista):
  """Function to find the main statistics of a list.

    Args:
        1st arg: A list of numbers that you want to analyze.
        
    Returns:
        Minimum value of the list
        Maximum value of the list
        Average value of the list
        Sum of all the values of the list
        """
  minimum=min(lista)
  maximum=max(lista)
  prom=round(mean(lista),2)
  suma=sum(lista)
  return(minimum,maximum,prom,suma)

summary=stats(lista)
print(f"""The statistics are: 
minimum: {summary[0]}
maximum: {summary[1]}
average value: {summary[2]}
sum of all values: {summary[3]}
In a list of {len(lista)} values
""")
