i=0
alt="testing"
new=""
for x in alt:
    if i%2 ==0:
        new+=x.upper()
    elif i%2==1:
        new+=x
    i+=1
    if i>len(alt):
        break
print(new)