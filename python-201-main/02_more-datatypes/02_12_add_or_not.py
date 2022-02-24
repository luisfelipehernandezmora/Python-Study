# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.
nums=set()
score=5
while score>0:
    ask=int(input("Give a number that you haven't gave yet "))
    if ask in nums:
        print(f"Hey! you gave that number already! You loose one point! You have {score-1} points left")
        print()
        score-=1
        continue
    else:
        nums.add(ask)
    if len(nums)>=10:
        print(f"Oh wow you gave +10 diferent numbers in less with still {score} points left!")
