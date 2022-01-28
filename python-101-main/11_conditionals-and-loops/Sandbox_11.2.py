number = int(input("Introduce a number to check wheter is divisible by 2 or 4 "))

if number % 4 == 0:
    print("divisible by four")
elif number % 2 == 0:
    print("divisible by two")
else:
    print("not divisible by two or four")