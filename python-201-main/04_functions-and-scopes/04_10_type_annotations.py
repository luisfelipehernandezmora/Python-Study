# Add type annotations to the three functions shown below.

def multiply(num1, num2):
    # This function takes to numbers and return the 
    # product of both of them
    return (num1 * num2)

def greet(greeting, name):
    # Compose a personalized greeting message to a specific person
    sentence = f"{greeting}, {name}! How are you?"
    # Returns a string with the message and name
    return (sentence)

def shopping_list(*args):
    # Creates a list using as many items you need in the list
    [print(f"* {item}") for item in args] #Prints the list on the CLI
    print()
    return (args) #In case is needed for something, it return the elements of the list in the form of a tuple

name=input("Hello! What's your name? ")
greeting="Oh, yoooouhoooo!"
hola=greet(greeting, name)
daily=int(input("How much is your daily salary? "))
days_by_week=int(input("And how many days a week you work? "))
salary=multiply(daily,days_by_week)


print(f"""
{hola} with a wage of {daily} and {days_by_week} days by week working, 
You have an income of {salary} for this week's purchases which are:
 """)
a=shopping_list("tomate","Zanahoria","pan","Y muchos colores!")

