# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"
strtup=tuple(string)
lista=[]
for ele in strtup:
    lista.append(ele)
for i in range(len(lista)):
    if lista[i]=="c":
        lista[i]="k"
final_tuple=tuple(lista)
print(f"The final tuple is {final_tuple}")
