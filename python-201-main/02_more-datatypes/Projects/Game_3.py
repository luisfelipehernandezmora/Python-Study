name=input("Hello! thanks for playing, what is your name? ")
sword=False
print(f"Hello {name}! Welcome to the game!")

Win_Game=False

while Win_Game==False:
    choice=str(input("Please choose between this 2 doors, left or right? ")).lower()
    
    if choice=="left":
        print(f"Al right {name}! you are in an empty room now! ")
        choice_left=input("You want to look around or go back? Yes(look around) or No(Go back)? ").lower()
        if choice_left=="yes":
            choice_sword=input("Hey, there is a sword there! Do you want to take it before you go back?? Yes or No? ").lower()
            if choice_sword=="yes":
                sword=True 
                print("Alright, nothing can stop you now, you have a good sword")
            elif choice_sword=="no":
                print("Alright then! Walk without the sword ")
            else:
                print("Well it seems that you are not sure of what to do, you better go back to the 2 doors")
                continue
        elif choice_left=="no":
            continue
        else:
            print("Well it seems that you are not sure of what to do, you better go back to the 2 doors")
    
    if choice=="right":
        print(f"My God {name}, there is a dragon here! ")
        choice_right=input("You want to kill the dragon or go back? Yes or No? ").lower()
        if choice_right=="yes":
            if sword:
                print(f"Hell Yeah {name}! You kill the dragon! ")
                Win_Game=True
                #break
            else:
                print("Oh No! You are eaten by the dragon, you lost the game :/ ")
                quit() #new position to exit the loop and the game
            #break
        elif choice_right=="no":
            print("Alright run back then!")
            continue
        else:
            print("Well it seems that you are not sure of what to do, you better go back to the 2 doors")
    
#if Win_Game:
print("Hey you won the game!")

#quit()
                