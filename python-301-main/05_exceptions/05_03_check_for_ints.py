# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

while True:
    try:
        ask=int(input(f"Give me a int: "))
        print("You see was no so hard! ")
        break
    except ValueError:
        print("it got it be an int ")