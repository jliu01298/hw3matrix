from display import *
from draw import *
from matrix import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()


'''add_edge(matrix,150,0,0,499,0,0)
add_edge(matrix,499,0,0,250,499,0)
add_edge(matrix,250,499,0,150,0,0)'''
w=0
x=0
y=0
z=0
for i in range(25):
    y=(y+176)%500
    z=(z+368)%500
    add_edge(matrix,w,x,0,y,z,0)
    w,x=y,z
else:
    add_edge(matrix,w,x,0,0,0,0)
draw_lines( matrix, screen, color )
display(screen)
