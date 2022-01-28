import pathlib

# path = pathlib.Path().cwd()

# for filepath in path.iterdir():
#     print(filepath)

# import pathlib

# path = pathlib.Path().cwd()
#a = pathlib.Path("C:\Users\Amma\Desktop") C:\Users\Amma\Desktop
a = pathlib.Path("D:\Luis Felipe")
#print(a)
new_path = pathlib.Path("D:\Luis Felipe\jpeg images folder")
new_path.mkdir(exist_ok=True)

for file in a.iterdir():
    if file.suffix==".jpeg":
        #print(file.stem)
        new_file_path=new_path.joinpath(file.name)
        file.replace(new_file_path)


# Identify the path to the folder, you have to import pathlib first
# Name all the files there
# Filter the files with some parameter
# move them in a new folder