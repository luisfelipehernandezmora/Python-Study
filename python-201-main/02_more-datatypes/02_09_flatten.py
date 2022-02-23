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

#starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
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
    #print(f"The flattened list is {flattened_list}")
    return(flattened_list)

# flat=flattener(starter_list)
# print(flat)

# Second complex way for deep lists
flattened_list=[]
for element in deep_list:
    eslista=False
    if isinstance(element,list):
        eslista=True

    if eslista==False:
        flattened_list.append(element)
        continue
    else:
        temp=flattener(element)
        flated=False
        temp=flattener(temp)
        while flated==False:
            temp2=[]
            for elem2 in temp:
                if type(elem2)==list:
                    temp=flattener(temp)
                    break
                elif type(elem2)!=list:
                    temp2.append(elem2)
            flated=True
        flattened_list.extend(temp2)
print(f"The flattened list is {flattened_list}")

                    

            


