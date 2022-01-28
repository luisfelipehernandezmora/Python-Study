name=input("Hello! thanks for playing, what is your name? ")
sword=False
print(f"Hello {name}! Welcome to the game!")

Win_Game=False

while Win_Game==False:
    choice=input("Please choose between this 2 doors, Left or Right? ")

    if choice=="Left":
        print(f"Al right {name}! you are in an empty room now! ")
        choice_left=input("You want to look around or go back? Yes(look around) or No(Go back)? ")
        if choice_left=="Yes":
            choice_sword=input("Hey, there is a sword there! Do you want to take it before you go back?? Yes or No? ")
            if choice_sword=="Yes":
                sword=True 
                print("Alright, nothing can stop you now, you have a good sword")
            elif choice_sword=="No":
                print("Alright then! Walk without the sword ")
    
    if choice=="Right":
        print(f"My God {name}, there is a dragon here! ")
        choice_right=input("You want to kill the dragon or go back? Yes or No? ")
        if choice_right=="Yes":
            if sword:
                print(f"Hell Yeah {name}! You kill the dragon! ")
                Win_Game=True
                break
            else:
                print("Oh No! You are eaten by the dragon, you lost the game :/ ")
            break
    
if Win_Game:
    print("Hey you won the game!")

quit()
                