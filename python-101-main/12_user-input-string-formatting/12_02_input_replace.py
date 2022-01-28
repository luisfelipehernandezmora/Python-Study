# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

text=input("Please put a sentence here: ")
symbol=input("type 1 symbol to make the sustitution ")
new=""
for char in text:
    if char==text[0]:
       new+=symbol
    else:
        new+=char
print(new) 