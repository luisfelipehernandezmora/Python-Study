# Save the user input options you allow e.g. in a set that you can check against when your user makes a choice. *
# Create an inventory for your player, where they can add and remove items.
# Players should be able to collect items they find in rooms and add them to their inventory.
# If they lose a fight against the dragon, then they should lose their inventory items.
# Add more rooms to your game and allow your player to explore.
# Some rooms can be empty, others can contain items, and yet others can contain an opponent.
# Implement some logic that decides whether or not your player can beat the opponent depending 
# on what items they have in their inventory
# Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. 
# This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.
import random
name=input("Hello! thanks for playing, what is your name? ")
print(f"Hello {name}! Welcome to the game!")
# Save the user input options you allow e.g. in a set that you can check against when your user makes a choice. *
answers={"yes","no","Yes","No","left","Left","right","Right","look around","go back","kill the dragon","go back"}
# Create an inventory for your player, where they can add and remove items.
inventory=set()
Win_Game=False

while Win_Game==False:
    mid=0
    print(f"Currently your inventory is {inventory}")
    choice=str(input("Please choose between this 5 doors, left, right, top, bottom or middle ? ")).lower()
    
    if choice=="left":
        print(f"Al right {name}! you are in an empty room now! ")
        choice_left=input("You want to look around or go back? Yes(look around) or No(Go back)? ").lower()
        if choice_left=="yes":
            choice_sword=input("Hey, there is a sword there! Do you want to take it before you go back?? Yes or No? ").lower()
            if choice_sword=="yes":
                inventory.add("sword")
                print("Alright, nothing can stop you now, you have a good sword")
            elif choice_sword=="no":
                print("Alright then! Walk without the sword ")
            else:
                print("Well it seems that you are not sure of what to do, you better go back to the 5 doors")
                continue
        elif choice_left=="no":
            continue
        else:
            print("Well it seems that you are not sure of what to do, you better go back to the 5 doors")
    
    if choice=="right":
        print(f"My God {name}, there is a dragon here! ")
        choice_right=input("You want to kill the dragon or go back? Yes or No? ").lower()
        if choice_right=="yes":
            if "WaterGun 95 efficient" in inventory:
                print("You have a water gun! You will take a probabilistic fight then")
                mid=random.randint(0,10)
                print(f"So your luck now was {mid}, in this case is needed more than 2 to beat him!")
                print(mid)
                if mid>2:
                    print("Hey you beat the dragon!")
                    break
                else:
                    print("oh no!, he beat you, you loose the game!")
                    quit()
            elif "sword" in inventory:
                print("ok, you have a sword to fight! You will take a probabilistic fight then")
                mid=random.randint(0,10)
                print(f"So your luck now was {mid}, in this case is needed more than 3 to beat him!")
                print(mid)
                if mid>3:
                    print("Hey you beat the dragon!")
                    break
                else:
                    print("oh no!, he beat you, you loose the game!")
                    quit()
            elif "batman" in inventory:
                print("ok, you don't have a sword but at least you already beat Batman! You will take a probabilistic fight then")
                mid=random.randint(0,10)
                print(f"So your luck now was {mid}, in this case is needed more than 7 to beat him!")
                print(mid)
                if mid>7:
                    print("Hey you beat the dragon!")
                    break
                else:
                    print("oh no!, he beat you, you loose the game!")
                    quit()
            else:
                print(f"ok you have not enough items, only {inventory}, you are killed by the dragon, you lost.")
                quit()
        elif choice_right=="no":
            print("Alright run back then!")
            continue
        else:
            print("Well it seems that you are not sure of what to do, you better go back to the 5 doors")
            continue
    if choice=="top":
        print(f"My God {name}, you come to the sky kingdom! There are many eagles! you want to take one with you? ")
        choice_top=input("Ok, so you have to be brave, you will need a sword but it will come alive with you, you will try? ").lower()
        if choice_top=="yes":
            if "sword" in inventory:
                print(f"Hell Yeah {name}! You impress that eagle, now it will acompany you in the quest! ")
                inventory.add("eagle")
                continue
            else:
                print("Oh No! They are flying too high to be catch! ")
                continue
        elif choice_top=="no":
            print("Alright run back then!")
            continue
        else:
            print("Well it seems that you are not sure of what to do, you better go back to the 5 doors")

    if choice=="bottom":
        print(f"Wow {name}, there is another player here! ")
        choice_right=input("You want to exchange some of your items with him/her? Yes or No? ").lower()
        if choice_right=="yes":
            if len(inventory)>0:
                give=input(f"So you can exchange one of the items: {inventory}! Choose wiselly! ")
                if give in inventory:
                    inventory.remove(give)
                    inventory.add("WaterGun 95 efficient")
            else:
                print(f"I am sorry {name} you still have no items to exchange with other players :/ ")
        elif choice_right=="no":
            print("Alright continue you way then! only thing, you will not be able to throw water to the dragon!")
            continue
        else:
            print("Well it seems that you are not sure of what to do, you better go back to the 5 doors")

    if choice=="midle":
        if "batman" in inventory:
            print("Hey you were here already! go back!")
            continue
        else:
            print(f"My God {name}, here is batman, and he wants to fight! ")
            if len(inventory)==0:
                print("ok, you have no items to fight! Eagles are good to figth Batman. you will take a probabilistic fight then")
                mid=random.randint(0,10)
                print(f"So your luck now was {mid}, in this case is needed more than 5 to beat him!")
                print(mid)
                if mid>5:
                    print("Hey you beat batman, you adquire one more level of strenght! ")
                    inventory.add("batman")
                    continue
                else:
                    print("oh no!, he beat you and as you have nothing, you loose the game!")
                    quit()
            else:
                if "eagle" in inventory:
                    print("hey you beat him inmediatelly! and you also upgrade one level! your eagle kill him")
                    inventory.add("batman")
                else:
                    print("ok, you have some items but not eagles! You will take a probabilistic fight then")
                    mid=random.randint(0,10)
                    print(f"So your luck now was {mid}, in this case is needed more than 2 to beat him!")
                    print(mid)
                    if mid>2:
                        print("Hey you beat batman, you adquire one more level of strenght! ")
                        inventory.add("batman")
                        continue   
#if Win_Game:
print("Hey you won the game!")

#quit()
                