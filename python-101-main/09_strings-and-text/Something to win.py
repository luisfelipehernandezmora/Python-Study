# TODO: Write a prompt that asks users to "type something to win"
#       They will only win if they type "something" into the prompt
#
# Collect user input
# Compare to the string "something"
# Print a win or lose message

a=input("type something to win: ")
a=a.lower()
if a=="something":
    print("Congratulations!")
else:
    print("Oh no!")
#str.endswith()
# str.capitalize()
# str.isdigit()
