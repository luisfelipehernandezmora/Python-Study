# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.
name=input("Hello, what is your name? ")
name1=name.split()
print(f"Hello {name1[0]}!, Thanks for coming")