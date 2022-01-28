# importing date class from datetime module
from datetime import date

age=input("Please insert your age: ")
age=float(age)
age=int(age)
print('''Next year you will be''', age+1 , '''   
Also you were born in''',date.today().year - age - 1)


  

# printing todays date
#print("Current date: ", todays_date)
  
# fetching the current year, month and day of today
#print("Current year:", todays_date.year)
##print(date.today().year)
#print("Current month:", todays_date.month)
#print("Current day:", todays_date.day)
