# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.

while True:
    try:
        num1=int(input(f"Please provide the number to be divided: "))
        num2=int(input(f"Please provide the number divide: "))
        res=num1/num2
        print(f"Your division is {res} yay!")
        break
    except ValueError:
        print(f"Upi have to enter numbers not something else")    
        continue
    except ZeroDivisionError:
        print(f"Oh nonono dont divide by zero, try again :D")
        continue