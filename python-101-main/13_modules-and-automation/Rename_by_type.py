import pathlib

folder=pathlib.Path("C:/Users/Amma/Desktop/Coding Nomads/python-101-main/13_modules-and-automation/Example for rename")
a=1
for file in folder.iterdir():
    old_name=file.stem
    old_ext=file.suffix
    c=file.suffix
    new_stem=f"This is the file {a} and now the format is {c}"
    new_name=new_stem+old_ext
    file.rename(pathlib.Path(folder,new_name))
    a+=1
