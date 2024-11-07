from Navigation.heading import Header


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
            if command == 'L':
                header = Header(header).left_new_heading()

            elif command == 'R':
                header = Header(header).right_new_heading()

        print(header)
