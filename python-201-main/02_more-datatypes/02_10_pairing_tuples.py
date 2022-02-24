# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.
from resources import randlist
a=randlist
print(a,"random list")
# Write your code below here

# sorts the numbers
sorted=sorted(a)
print(sorted,"sorted","length",len(sorted))

# stores the numbers in tuples of two in a new list
list_of_tuples=[]
i=0
while i<len(sorted):
    if i>=len(sorted):
        break
    if i<=len(sorted)-2:
        tup=(sorted[i],sorted[i+1])
        list_of_tuples.append(tup)
        i+=2
    if i==len(sorted)-1:
        tup=(sorted[i],)
        list_of_tuples.append(tup)
        break
print(list_of_tuples)
# prints each tuple
for elem in list_of_tuples:
    print(f"{elem}")