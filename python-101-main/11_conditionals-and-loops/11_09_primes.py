# Print out every prime number between 1 and 1000.
lower=int(input("Introduce the lower number of the prime interval: "))  
upper=int(input("Introduce the upper number of the prime interval: "))  
prime=[]
print("The prime numebrs betweeen",lower,"and",upper,"is: ")

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            prime.append(num)
print(prime)            
    

