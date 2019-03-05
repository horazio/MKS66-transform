from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge mGoes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:atrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):

    with open(fname) as file:
        fd = file.read()
    fd = fd.split("\n")

    for i in range(len(fd)):
        x = fd[i]

        if(x == "line"):
            x = fd[i + 1].split()
            add_edge(points, int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]))

        if(x == "ident"):
            ident(transform)

        if(x == "scale"):
            x = fd[i + 1].split()
            matrix_mult(make_scale(int(x[0]), int(x[1]), int(x[2])), transform)

        if(x == "move"):
            x = fd[i + 1].split()
            matrix_mult(make_translate(int(x[0]), int(x[1]), int(x[2])), transform)

        if(x == "rotate"):
            x = fd[i + 1].split()
            if(x[0] == "x"):
                matrix_mult(make_rotX(int(x[1])), transform)
            if(x[0] == "y"):
                matrix_mult(make_rotY(int(x[1])), transform)
            if(x[0] == "z"):
                matrix_mult(make_rotZ(int(x[1])), transform)

        if(x == "apply"):
            matrix_mult(transform, points)

        if(x == "display"):
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)

        if(x == "save"):
            x = fd[i + 1].split()

            clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(screen, x[0])

        if(x == "quit"):
            return None
