# Write a script that moves all files with the .png extension
# from one folder to another
# Import pathlib
# Find the path to my Desktop
# Create a new folder
# Filter for screenshots only
# Create a new path for each file
# Move the screenshot there
import pathlib
folder=pathlib.Path("/home/luisfelipe/Coding Nomads/python-101-main/projects/move_files_from_here")
destination=pathlib.Path("/home/luisfelipe/Coding Nomads/python-101-main/projects/move_here")
destination.mkdir(exist_ok=True)
for files in folder.iterdir():
    ext=files.suffix    
    if ext==".PNG":
        new_name=destination.joinpath(files.name)
        files.replace(new_name)
#done