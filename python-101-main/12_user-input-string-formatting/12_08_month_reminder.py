# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.
num=int(input("introduce a number between 1 and 12 for getting a month "))
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
cond=False
while cond==False:
    num=int(input("Error, please introduce a number between 1 and 12 for getting a month "))    
    if 0<num<13:   
        cond=True

print(months[num-1])