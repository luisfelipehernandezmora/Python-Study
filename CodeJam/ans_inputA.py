from pprint import pprint
class contributor:
    """Class to define a contributos

    Args:
        1st arg: name
        2nd arg: quality 
        3rd arg: level   
                
    Returns:
        A contributor object with the quality and it's level
        """
    def __init__(self,name,quality,level):
        self.name=name
        self.quality=quality
        self.level=level
    def __str__(self) -> str:
        return(f"Contributor(name:{self.name}, quality:{self.quality}, level:{self.level})")

class project:
    """Class to define a project

    Args:
        1st arg: name
        2nd arg: days to complete
        3rd arg: max score   
        4th arg: best before day
        5th arg: contributors required
                
    Returns:
        A project object with the information about the project
        """
    def __init__(self,name,days_req,score,best_before,contr_req):
        self.name=name
        self.days_req=days_req
        self.score=score
        self.best_before=best_before
        self.contr_req=contr_req
    def __str__(self) -> str:
        return(f"Project(name:{self.name}, days_req:{self.days_req}, score:{self.score},best_before:{self.best_before}, contr_req:{self.contr_req})")

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
book_of_people=[]
portfolio=[]
solve=[]
j=1
cerrar=0
cerrar+=int(contributors)
while contributing:
    person=clean[j].split(" ",2)
    name=person[0]
    qualities=person[1]
    cerrar+=int(qualities)
    for x in range(int(qualities)):
        j+=1
        quality=clean[j].split(" ",2)
        nameq=quality[0]
        level=quality[1]
        persona=contributor(name,nameq,level)
        book_of_people.append(persona.__str__())
    j+=1
    if j>cerrar:
        contributing=False
        break
#pprint(book_of_people)
#Now we will create the project objects
for z in range(cerrar+1,len(clean)):
    item=clean[z].split(" ",5)
    if len(item)==5:
        namep=item[0]
        days_req=item[1]
        score=item[2]
        best_before=item[3]
        contr_req=item[4]    
        proyecto=project(namep,days_req,score,best_before,contr_req)
        portfolio.append(proyecto)
        for x in range(int(contr_req)):
            z+=1
            quality=clean[z].split(" ",2)
            nameq=quality[0]
            level=quality[1]
            resolv=contributor(namep,nameq,level)
            solve.append(resolv.__str__())
    z+=1
pprint(solve)