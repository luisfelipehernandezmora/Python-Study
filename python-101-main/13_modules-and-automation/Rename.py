import pathlib

folder=pathlib.Path("C:/Users/Amma/Desktop/Coding Nomads/python-101-main/13_modules-and-automation/Example for rename")
a=2
for file in folder.iterdir():
    #print(file.stem)
    
    old_name=file.stem
    old_ext=file.suffix
    #print(new_name)
    #directory=folder.parent
    new_stem=f"test {a}"
    new_name=new_stem+old_ext
    file.rename(pathlib.Path(folder,new_name))
    a+=1
    #print(a)
