# CHALLENGE: Write a script that sorts a dictionary into a
# list of tuples based on the dictionary's values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
# result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

# Check out the Python docs and see whether you can come up with a solution,
# even if you don't yet completely understand why it works the way it does:
# https://docs.python.org/3/howto/sorting.html#key-functions
# Feel free to discuss any questions you have with your mentor and on the forum!
tuples=()
list_of_tuples=[]
valores=[]
for value in input_dict.values():
    valores.append(value)
orden=sorted(valores)
i=0
while len(list_of_tuples)<3:
    for key in input_dict.keys():
        if input_dict[key]==orden[i]:
            tuples=(key,orden[i])
            list_of_tuples.append(tuples)
            i+=1
            tuples=()
        if i==3:
            i=0
        if len(list_of_tuples)>=3:
            break
print(list_of_tuples)


