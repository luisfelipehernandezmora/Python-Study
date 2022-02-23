# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list1= [1, 2, 3, 4, 3, 4, 5]
# Way 1: To convert into a set type
only=set(list1)
print(f"first way, with a set {only}")

# Way 2: Loop and a second list
lista2=[]
for elem in list1:
    if elem in lista2:
        continue
    lista2.append(elem)
print(f"second way, with a loop and a second list {lista2}")