# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich (bread, *topings):
    """Function to make a nice meal with bread.

    Args:
        1st argument: The bread or new idea you want to bring in your meal.
        2nd argument: All the topings you want to put to it.
        
    Returns:
        A Sandwich!.
        """
    add=""
    for arg in topings:
        add+=arg+" and \n"      
    meal=f"""So it seems you are hungry! your treat will be:
{bread}
{add}one more {bread} (just to make it a normal sandwich :p)
"""
    return(meal)
eat=make_sandwich("bread","common sense","peace for today","cease the fire","war have no winners")
print(eat)