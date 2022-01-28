opinion=input("Introduce your opinion please: ")
opinion_low=opinion.lower()
answer=""
for i in range(len(opinion)):
    if i%2==0:
        answer+=opinion_low[i].upper()
    else:
        answer+=opinion_low[i]
print(answer)
a=int(input("Put a number" ))
b=a**2
print(b)