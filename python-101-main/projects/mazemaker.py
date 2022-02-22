# Challenge yourself and practice learning from outside resources
# by following this tutorial to build a maze generator:
# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e
from colorama import init, Fore
from pprint import pprint
init()
def init_maze(width, height):
    maze=[]
    for i in range(0, height):
        line=[]
        for j in range(0, width):
            line.append("u")
        maze.append(line)
    return(maze)

def print_maze(maze):
    for i in range(0,len(maze)):
        for j in range(0,len(maze[0])):
            if maze[i][j]=="u":
                print(Fore.RED,f"{maze[i][j]}",end="")
            elif maze[i][j]=="w":
                print(Fore.CYAN,f"{maze[i][j]}",end="")
            else:
                print(Fore.YELLOW,f"{maze[i][j]}",end="")



lab=init_maze(5,5)
pprint(lab)
