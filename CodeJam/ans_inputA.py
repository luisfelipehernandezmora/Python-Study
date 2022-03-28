class contributor:
    """Class to define Menu items of a restaurant

    Args:
        1st arg: name
        2nd arg: veg or non veg 
        3rd arg: calories
        4th arg: price     
                
    Returns:
        A list of information of the country in order: [name, veg/non veg, calories, price]
        """




    

folder="/home/luisfelipe/Coding Nomads/CodeJam/a_an_example.in.txt"
clean=[]
with open (folder,"r") as file:
    data=file.readlines()
#print(data,"\n")
#Present the data cleaner ready to split in components
for i in data:
    a=i[:-1]
    clean.append(a)
print(clean,"\n")
#Find how many people and projects you have in front
info=clean[0].split(" ",2)
contributors=info[0]
projects=info[1]
print(f"info:{info}, contributors={contributors}, projects={projects}")
#Now you must use a flag to know when you finished with the contributors
contributing=True
j=1
while contributing:
    person=data[j].split(" ",2)
