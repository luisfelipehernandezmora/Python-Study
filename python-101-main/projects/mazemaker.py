# Challenge yourself and practice learning from outside resources
# by following this tutorial to build a maze generator:
# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e
import random
from colorama import init, Fore

init()
cell = "c"
wall = "w"
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
                print(Fore.LIGHTGREEN_EX,f"{maze[i][j]}",end="")
            elif maze[i][j]=="w":
                print(Fore.RED,f"{maze[i][j]}",end="")
            else:
                print(Fore.YELLOW,f"{maze[i][j]}",end="")
        print()
width=20
height=12
maze=init_maze(width,height)
print_maze(maze)
#pprint(lab)
starting_height=int(random.random()*height)
starting_width=int(random.random()*width)

#To make sure we are not started in the border, we aply:
if starting_height==0:
    starting_height+=1
elif starting_height==height-1:
    starting_height-=1

if starting_width==0:
    starting_width+=1
elif starting_width==width-1:
    starting_width-=1

# Now we pick this random cell, and will surrounded by walls
maze[starting_height][starting_width]=cell
walls=[]
walls.append([starting_height-1,starting_width])
walls.append([starting_height+1,starting_width])
walls.append([starting_height,starting_width+1])
walls.append([starting_height,starting_width-1])

maze[starting_height-1][starting_width]=wall
maze[starting_height+1][starting_width]=wall
maze[starting_height][starting_width-1]=wall
maze[starting_height][starting_width+1]=wall

while walls:
    rand_wall=walls[int(random.random()*len(walls))-1]
    #we check if the visited random remaining wall is surrounded by unvisited cells, 4 cases:
    if rand_wall[1]!=0:
        if maze[rand_wall[0]][rand_wall[1]-1]=="u" and maze[rand_wall[0]][rand_wall[1]+1]=="c":
    if rand_wall[1]!=width-1:
        if maze[rand_wall[0]][rand_wall[1]+1]=="u" and maze[rand_wall[0]][rand_wall[1]-1]=="c":
    if rand_wall[0]!=0:
        if maze[rand_wall[0]+1][rand_wall[1]]=="u" and maze[rand_wall[0]-1][rand_wall[1]]=="c":
    if rand_wall[0]!=height-1:
        if maze[rand_wall[0]-1][rand_wall[1]]=="u" and maze[rand_wall[0]+1][rand_wall[1]]=="c":

