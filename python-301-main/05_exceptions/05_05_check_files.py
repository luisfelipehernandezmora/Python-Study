# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.
import os
import random

file_name = 'integers.txt'
while True:
    # ask=input("which file you want to open: ")
    try:
        folder=os.getcwd()+f"/python-301-main/05_exceptions/integers.txt"
        with open (folder,"r") as file:
            reading=file.readlines()
        numbers=[]
        for each in reading:
            if len(each)>1:
                each=each[:-1]
                numbers.append(each)
            else:
                numbers.append(each)
    except FileNotFoundError:
        print("The desired file name doesn't seem to match, try again please")
    try:
        nums=random.sample(numbers,3)
        nums2=[]
        for num in nums:
            num=int(num)
            nums2.append(num)
        result=(nums2[0]-nums2[1])/nums2[2]
        print(f"The random numbers are: {nums2}")
        print(f"The result is: {result}")
        break
    except ZeroDivisionError:
        print(f"oh it seems you want to divide by zero with {nums2}, let's just go again")
        continue

