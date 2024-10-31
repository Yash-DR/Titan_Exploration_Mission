"""The robots starting position and location are represented by a grid of squares, which cover Titan's surface, and a compass direction (N,E, S, W)
A robots position and location is represented by a combination of x and y and a letter representing one of the four cardinal compass points
Surface is divided into grids
L, R and M input strings which represents 90 degree spin in left or right and m represent movement by one grid point
The first line of input is upper right co-ordinate of plateau., the lower left co-ordinates are assumed to be 0,0.
The first line gives the robot position, and the second line is a series of instructions telling the robot how to explore the plateau.
The position is made up of 2 letters and a letter separated by spaces"""

from heading import left_heading, right_heading
from movement import new_coordinates


xy = input("Upper right co-ordinates - ")
x_ord = None
y_ord = None
if len(xy) == 2:
    lower_left_ord = [0,0]
    upper_right_ord = [xy[0], xy[1]]
    x_ord_max = xy[0]
    y_ord_max = xy[1]

    co_ordinates = input("Enter the co-ordinates of the robot - ")
    if len(co_ordinates) == 3:
        x_ord = co_ordinates[0]
        y_ord = co_ordinates[1]
        heading = co_ordinates[2]

        exploration_values = input("Enter the instructions to explore the plateau - ")

        for i in exploration_values:
            if i.lower() == 'l':
               heading = left_heading(heading)
            elif i.lower() == 'r':
                heading = right_heading(heading)
            elif i.lower() == 'm':
                x_ord, y_ord = new_coordinates(x_ord_max, y_ord_max, x_ord, y_ord, heading)

        print(f"New co-ordinates are {x_ord}{y_ord}{heading.upper()}")

    else:
        print("Invalid Robot co-ordinates")

else:
    print("invalid co-ordinates")
