#method that allows you to determine at what index position a certain sub-string exists.

fullstring = "StackAbuse"
substring = "tack"

try:
    fullstring.index(substring)
except ValueError:
    print("Not found!")
else:
    print("Found!")

print(fullstring.index(substring))
#is the same to say
print("StackAbuse".index("tack"))

#method to check whether a string starts with a certain sub-string.

message = 'Python is fun'
# check if the message starts with Python
print(message.startswith('Python'))
#is the same to say
print('Python is fun'.startswith('Python'))
