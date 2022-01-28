# Hard-code a word that needs to be guessed in the script
# Print an explanation to the user
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it
import string
def indexes(my_list, desired_element):
    return [index for index, element in enumerate(my_list) if element == desired_element]
word="neumatic"
w2=list(word)

print("So here is the game: There is a hidden word, and you have to guess \
it's components in certain amount of atempts")
status=""
counter=8
alphabet_string = string.ascii_lowercase

for char in word:
    status+='_'
w=list(status)
print(w)
while counter>0:
    ask=(input("Try to guess one of the letters of the secret word ")).lower()
    if ask in alphabet_string:
        #print("you are in the right way")
        if ask in word:
            c=indexes(w2,ask)
            #print(c)
            for i in c:
                w[i]=ask
            if "".join(w)==word:
                break
        else:
            counter-=1
        print(w)
        print(f"You have {counter} mistaken attempts left")
if counter==0:
    print("You lost, want to try it again?")
else:
    print(f"Hey you won! you find that '{word}' is the correct word")
