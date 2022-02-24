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

#First simple way for shallow lists
def flattener(lista):
    """"Flatens shallow lists"""
    flattened_list=[]
    for element in lista:
        if isinstance(element,list):         #Check if it a list or another data type
            flattened_list.extend(element)   # As is a list, just included fully .extend() instead of .append()
        else:
            flattened_list.append(element)
    return(flattened_list)

flat=flattener(starter_list)
print(f"The flattened list is {flat} in the shallow case")

# Second complex way for deep lists
flattened_list=[]
for element in deep_list:
    eslista=False
    if isinstance(element,list):           #Check if it's a list
        eslista=True                       #Use this flag to aply selective treatment depending on the data type

    if eslista==False:
        flattened_list.append(element)     #Include the element since is not a list
        continue                           #Begin again with the next element
    else:
        temp=flattener(element)            #Since we know is a list already, we apply the function again to make it level more shallow
        flated=False                       #We still don't know if it's the list is still deeper
        while flated==False:
            temp2=[]
            for elem2 in temp:
                if type(elem2)==list:      #We discover again is a list, meaning it was still deep
                    temp=flattener(temp)   #Apply the function again 
                    break                  #Began again now with one level less in the list
                elif type(elem2)!=list:
                    temp2.append(elem2)    #So far seems there is not inner lists, so collect those values 
            flated=True                    #If managed to go trought the whole loop
            flattened_list.extend(temp2)

print(f"The flattened list is {flattened_list} in the deep case")

                    

            


