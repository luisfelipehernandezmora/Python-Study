#Tasks
# Think of a logical comparison that uses at least two different logical operators and implement it in code.

p=float(input("Introduce the power of your equipment in Watts: "))

if p<1200:
   p=True
else:
   p=False

b=float(input("Introduce the Amperage of your breaker in Amperes "))

if b==20:
   b=True
else:
   b=False

if p and b:
    print("You are using safe conections!")
else:
    print("Hey dude, better call an engineer to check your instalations ;)")    
            