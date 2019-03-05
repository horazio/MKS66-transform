from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 255, 10, 10 ]
edges = []
transform = new_matrix()

'''
#makes other image

ident(transform)

all = []
A = []

add_edge(A, 500, 0, 25, 500, 50, 25)
add_edge(A, 500, 50, 25, 450, 50, 25)
add_edge(A, 450, 50, 25, 450, 0, 25)
add_edge(A, 450, 0, 25, 500, 0, 25)

add_edge(A, 500, 0, -25, 500, 50, -25)
add_edge(A, 500, 50, -25, 450, 50, -25)
add_edge(A, 450, 50, -25, 450, 0, -25)
add_edge(A, 450, 0, -25, 500, 0, -25)

add_edge(A, 500, 0, 25, 500, 0, -25)
add_edge(A, 500, 50, 25, 500, 50, -25)
add_edge(A, 450, 50, 25, 450, 50, -25)
add_edge(A, 450, 0, 25, 450, 0, -25)


matrix_mult(make_rotY(10), transform)
matrix_mult(make_rotZ(5), transform)
matrix_mult(make_rotX(20), transform)



for i in range(50):
    for pt in A:
        all.append(pt[:])
    matrix_mult(transform, A)

draw_lines(all, screen, color)
save_extension(screen, 'img.png')
'''

parse_file( 'script', edges, transform, screen, color )
