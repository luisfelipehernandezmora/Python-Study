# #Find the maximun and minimum 
# import csv
# import numpy as np
 
# with open('Bitcoin price quest.csv', 'r') as f:
#     data = list(csv.reader(f, delimiter=","))

# data = np.array(data)
# a=float(data[3][1])
# a=round(a,2)
# mini=0
# maxi=0
# values=[]
# for x in data:
#     value=float(x[1])
#     values.append(value)
#     mini=min(values)
#     maxi=max(values)
    
# print(f"The minimum price of BTC in this period was {mini} and the highest {maxi}")

from datetime import date
# datetime(YYYY,MM,DD)
# aries 3-21 to 4-19
aries_start = date(1, 3, 21)
aries_end = date(2100, 4, 19)
birthday = date(2001, 3, 29)
#if aries_start.month.day <= birthday.month.day <= aries_end.month.day:
if aries_start<= birthday<= aries_end:

    print("You're an aries!")