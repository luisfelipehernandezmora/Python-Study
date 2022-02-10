# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. 
# They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.
import requests

url="https://uzby.com/api.php?min=4&max=10" #Get a random name for the user
name=requests.get(url).text
sword=False
print(f"Hello, today your name will be {name}! Welcome to the game!")

choice=input("Please choose between this 2 doors, Left or Right? ") 

if choice=="Left":
    print("Al right! you are in an empty room now! ")
    choice_left=input("You want to look around or go back? Yes(look around) or No(Go back)? ")
    if choice_left=="Yes":
        choice_sword=input("Hey, there is a sword there! Do you want to take it?? Yes or No? ")
        if choice_sword=="Yes":
            sword=True
        else:
            print("Alright then! Walk without the sword ")

    choice=input("Please choose between this 2 doors, Left or Right? ")

if choice=="Right":
    print("My God, there is a dragon here! ")
    choice_right=input("You want to kill the dragon or go back? Yes or No? ")
    if choice_right=="Yes":
        if sword:
            print("Hell Yeah! You kill the dragon! ")
        else:
            print("Oh No! You are eaten by the dragon, you lost the game :/ ")
    else:
        go_back_right=input("You want to go back? ")
        if go_back_right=="Yes":
            choice=input("Please choose between this 2 doors, Left or Right? ")
        
quit()