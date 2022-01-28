# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.
import math
inv=int(input("What is your investment amount? "))
inv_rate=float(input("What is your investmet rate in %? "))
year=int(input("For how many years? "))

print(f"Your profits will be {math.trunc(inv*inv_rate*year/100)}")