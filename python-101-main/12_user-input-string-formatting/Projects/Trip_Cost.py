km=int(input("How long you have to drive? "))
eficiency=int(input("How many Km/liter your car do? "))
price=int(input("How much is 1 liter of fuel? Dont put currency symbols please "))
currency=input("Insert the currency symbol ")

cost=int(km/eficiency*price)

print(f"The cost of your trip is {currency}{cost}  for a journey of {km} km \
with a car of the eficiency {eficiency} km/liter and with a fuel price of {currency}{price} by liter")