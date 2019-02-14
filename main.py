from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()


add_edge(matrix,4,0,0,499,0,0)
add_edge(matrix,499,0,0,250,499,0)
add_edge(matrix,250,499,0,0,0,0)

draw_lines( matrix, screen, color )
display(screen)
