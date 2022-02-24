# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}
new={}
key_dict1=dict_1.keys()
key_dict2=dict_2.keys()
print(key_dict1, key_dict2)
for key in dict_1.keys():
    if key in dict_2.keys():
        new[key]=dict_1[key]+dict_2[key]
    else:
        new[key]=dict_1[key]
for key in dict_2.keys():
    if key in dict_1.keys():
        continue
    else:
        new[key]=dict_2[key]

print(new)
