# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

print(randlist)
largest=max(randlist)
print(largest, "largest")
prod=1
for i in randlist:
    prod=prod*i
print(prod,"product")