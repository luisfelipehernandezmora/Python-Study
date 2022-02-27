# Fix the code below to make it possible to print out
# the uppercase copy of the name.
# - use `return` to create an output for the function
# - assign the output to a variable
# - print that variable
import requests
def name_gen():
    """Function to find random names

    Args:
        None
        
    Returns:
        A random name
    """
    url="https://uzby.com/api.php?min=4&max=10" #Get a random name for the user
    name=requests.get(url).text
    return(name)

def shout(name):
    loud_name = name.upper()
    return(loud_name)

name=name_gen()
message=shout(name)
print(message)
