from Navigation.heading import Header
from Navigation.robot_movement import RobotMovement


class Navigation:
    def __init__(self, robot_coordinate, command):
        self.robot_coordinate = robot_coordinate
        self.robot_command = command


    def new_coordinates(self):
        x_coord = self.robot_coordinate[0]
        y_coord = self.robot_coordinate[1]
        header = self.robot_coordinate[2]

        new_coord = (x_coord, y_coord, header)

        for command in self.robot_command:
            # Get the new direction of the robot if the command is Left
            if command == 'L':
                header = Header(header).left_new_heading()

            # Get the new direction of the robot if the command is Right
            elif command == 'R':
                header = Header(header).right_new_heading()

            # Get the new position of the robot along x and y coordinates if the command is 'M' or Movement
            elif command == 'M':
                x_coord, y_coord = RobotMovement(x_coord, y_coord, header).new_robot_position()

        # Updating the final coordinates and header for the robot after executing the command
        new_coord = (x_coord, y_coord, header)

        return new_coord
