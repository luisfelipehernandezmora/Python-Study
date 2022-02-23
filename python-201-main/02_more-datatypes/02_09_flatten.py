# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
deep_list=[1,[2,4,"word"],"another word",[1,2,3,[10,11,12,[100,200]]],3,"happy ending",[-1,-2,[-10,-20,[1000]]]]

# First simple way for shallow lists
def flattener(lista):
    """"Flatens shallow lists"""
    flattened_list=[]
    for element in lista:
        if isinstance(element,list):
            flattened_list.extend(element)
        else:
            flattened_list.append(element)
    print(f"The flattened list is {flattened_list}")
    return(flattened_list)

flat=flattener(starter_list)
print(flat)

# for element in starter_list:
#     eslista=True
#     if isinstance(element,list):
#         eslista=False