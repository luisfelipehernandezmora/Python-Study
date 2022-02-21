# Move and rename all .png files on your Desktop
# Identify all screenshots on your Desktop
# Create a new directory
# Move and rename all screenshots
import pathlib
folder=pathlib.Path("/home/luisfelipe/Coding Nomads/python-101-main/projects/move_here")
i=0
for file in folder.iterdir():
    if file.suffix==".PNG":
        new_name=folder.joinpath("Captura "+str(i)+".PNG")
        file.replace(new_name)
        i+=1
