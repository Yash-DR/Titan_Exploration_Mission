"""The robots starting position and location are represented by a grid of squares, which cover Titan's surface, and a compass direction (N,E, S, W)
A robots position and location is represented by a combination of x and y and a letter representing one of the four cardinal compass points
Surface is divided into grids
L, R and M input strings which represents 90 degree spin in left or right and m represent movement by one grid point
The first line of input is upper right co-ordinate of plateau., the lower left co-ordinates are assumed to be 0,0.
The first line gives the robot position, and the second line is a series of instructions telling the robot how to explore the plateau.
The position is made up of 2 letters and a letter separated by spaces"""

from heading import left_heading, right_heading
from movement import new_coordinates

num_of_robots = input("Enter the number of Robots - ")
xy = input("Upper right co-ordinates - ")
x_ord = []
y_ord = []
heading = []
exploration_values = []
x_ord_max = None
y_ord_max = None

if len(xy) == 2:
    lower_left_ord = [0, 0]
    upper_right_ord = [xy[0], xy[1]]
    x_ord_max = xy[0]
    y_ord_max = xy[1]

    for i in range(int(num_of_robots)):
        co_ordinates = input(f"Enter the co-ordinates of the Robot-{i+1} - ")
        if len(co_ordinates) == 3:
            x_ord.append(co_ordinates[0])
            y_ord.append(co_ordinates[1])
            heading.append(co_ordinates[2])

            navigation = input("Enter the instructions to explore the plateau - ")
            exploration_values.append(navigation)

        else:
            print("Invalid Robot co-ordinates")

else:
    print("invalid co-ordinates")

for j in range(int(num_of_robots)):
    try:
            for i in exploration_values[j]:
                if i.lower() == 'l':
                    heading[j] = left_heading(heading[j])
                elif i.lower() == 'r':
                    heading[j] = right_heading(heading[j])
                elif i.lower() == 'm':
                    x_ord[j], y_ord[j] = new_coordinates(x_ord_max, y_ord_max, x_ord[j], y_ord[j], heading[j])

            print(f"New co-ordinates for Robot-{j+1} is {x_ord[j]}{y_ord[j]}{heading[j].upper()}")

    except:
        print(f"Cannot find the co-ordinates for Robot-{j+1} due to incorrect inputs")

