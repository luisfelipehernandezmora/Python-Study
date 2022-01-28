# Which of the following strings is the longest?
# Use the len() function to find out.

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"

a=len(longest_german_word)
b=len(longest_hungarian_word)
c=len(longest_finnish_word)
d=len(strong_password)

print(a)
print(b)
print(c)
print(d)

length=[a,b,c,d]
# sorting the list
length.sort()
# printing the last element
print("Largest element is:", length[-1])

if a>b and a>c and a>d:
    print("The longest_german_word is the largest!")
if b>a and b>c and b>d:
    print("The longest_hungarian_word is the largest!")
if c>b and c>a and c>d:
    print("The longest_finnish_word is the largest!")
if d>b and d>c and d>a:
    print("The strong_password is the largest!")        
