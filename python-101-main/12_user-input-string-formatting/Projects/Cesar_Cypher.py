import string
alphabet_string = string.ascii_lowercase
alphabet = list(string.ascii_lowercase)
#print(alphabet)
text=input("Write your text you want to cypher ").lower()
num=int(input("Write of how many spaces you want to cypher your text "))
new=""
for char in text:
    if char in alphabet:   
        a=alphabet.index(char)
        b=alphabet[a-num]
        new+=b
    else:
        new+=char
print(new)
