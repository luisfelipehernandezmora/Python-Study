# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings
text1=input("Insert your first string ")
text2=input("Insert your second string ")
text3=input("Insert your third string ")

opt1=[text1,text2,text3]

a=len(text1)
b=len(text2)
c=len(text3)

opt2=[a,b,c]

if a>b and a>c:
    print(a,text1)
elif c>b and c>a:
    print(c,text3)
elif b>a and b>c:
    print(b,text2)