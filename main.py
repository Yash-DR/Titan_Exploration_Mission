"""The robots starting position and location are represented by a grid of squares, which cover Titan's surface, and a compass direction (N,E, S, W)
A robots position and location is represented by a combination of x and y and a letter representing one of the four cardinal compass points
Surface is divided into grids
L, R and M input strings which represents 90 degree spin in left or right and m represent movement by one grid point
The first line of input is upper right co-ordinate of plateau., the lower left co-ordinates are assumed to be 0,0.
The first line gives the robot position, and the second line is a series of instructions telling the robot how to explore the plateau.
The position is made up of 2 letters and a letter separated by spaces"""


from Grid.grid import GridBoundary
from Navigation.navigation import Navigation


def main():
    # Defining Input Values
    total_grid_size = (5, 5)
    robot_initial_coordinate = [('1', '2', 'N'), ('3', '3', 'E')]
    robot_commands = ["LMLMLMLMM", "MMRMMRMRRM"]

    # Check if the robot initial_coordinate position is within the grid
    for coordinate in robot_initial_coordinate:
        position = GridBoundary(total_grid_size).coordinate_position(coordinate)
        if position:
            index = robot_initial_coordinate.index(coordinate)
            # Get the new coordinates of the robot
            robot_final_coordinate = Navigation(coordinate, robot_commands[index]).new_coordinates()

            print(robot_final_coordinate)


if __name__ == "__main__":
    main()

