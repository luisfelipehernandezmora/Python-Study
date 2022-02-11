# Add the code for the file counter script that you wrote in the course.
import pathlib
#  \\wsl$\Ubuntu-20.04\home\luisfelipe\Coding Nomads\python-201-main\projects
folder=pathlib.Path("/home/luisfelipe/Coding Nomads/python-201-main/projects")
#for file in folder.iterdir():

a=["dot.txt", "image.png", "python.20.32.19.py"]
extensiones=set()
cantidades=dict()
#for x in a: 
for file in folder.iterdir():
        file_name=file.name
        c=file_name.split(".") 
        ext="."+c[-1]
        #print(c,ext) 
        extensiones.add(ext)
        
print(extensiones)
