#flag = True

#if flag == True:
   # print("yay!")

#Add a second conditional statement to the code snippet above that executes only if the flag variable is False.
#Run the code and confirm that the second print() statement doesn't get executed.
#Now add a line to your first conditional statement that changes the value of flag to False in the indented code block.
#Run the code again and confirm that both print() statements now get executed.
flag = True

if flag == True:
    print("yay!")
    flag = False
elif flag == False:
    print("Yay!")

hunger =str(input("How hungry are you? "))

if hunger == "big":
    print("Eat the pizza")
elif hunger == "small":
    print("Eat the apple")
elif hunger == "medium":
    print("Eat the apple and a little of the pizza, maybe?")
elif hunger == "giant":
    print("Eat the apple and the pizza, and drink some water also!")
else:
    print("Don't eat anything")

