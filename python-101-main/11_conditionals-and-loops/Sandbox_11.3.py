secret = "2349H30023388281E3299371l1l3094842O0333322883"
solution = ""

for cha in secret:
    if cha.isalpha():
        solution += cha

print(solution)

#Tasks
# Apply a string method to each of the characters in a string.
# Apply alternating string methods to every second character in your string.
# Create a for loop that prints out aLtErNaTiNg CaPs from the word you iterate over.

text=str(input("Please write whatever you will like to turn in to alternate caps "))
#print(text.upper())
answer=""
x=0
for char in text:
   if x<len(text)-2:
    char=text[x].upper()
    answer+=char
    answer+=text[x+1]
    x=x+2
print(answer)

for n in range(100):
    if n % 2 == 0:
        print(n)