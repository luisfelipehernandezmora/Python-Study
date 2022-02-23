# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]
word=input("Insert your phrase to separate in a list of tuples: ")
lista=[]
result_list=[]
lista=word.split(" ")
for item in lista:
    x=tuple(item)
    result_list.append(x)
print(f"The result list is {result_list}")


