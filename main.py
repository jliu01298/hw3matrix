from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
_matrix=[]

add_edge(matrix,0,0,0,25,0,0)
add_edge(matrix,25,0,0,25,25,0)
add_edge(matrix,25,25,0,0,25,0)
add_edge(matrix,0,25,0,0,0,0)
add_edge(_matrix,6,4,0,8,13,0)
add_edge(_matrix,14,13,0,25,6,0)
add_edge(_matrix,23,21,0,29,25,0)
add_edge(_matrix,11,15,0,13,17,0)
draw_lines( matrix, screen, color )
matrix_mult(_matrix,matrix)
draw_lines( matrix, screen, color )
display(screen)

