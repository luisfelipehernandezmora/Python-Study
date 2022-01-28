# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"
extension=""
ext_found=False
#print(filename.index('.')) #To know in which index position is 
for char in filename:       
    if char==".":
        ext_found=True       
    if ext_found:
        extension+=char
#print(extension)
if extension==".pdf":
    print("Your document is a:",extension)


# x=0
# suma=0
# while x<101:
#     suma+=x
#     x+=1
#     print(suma)

    



