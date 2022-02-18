from PIL import Image        
import pathlib
path=pathlib.Path("/home/luisfelipe/Coding Nomads/python-101-main/projects/test")                                                              
img = Image.open(path)
img.show()
