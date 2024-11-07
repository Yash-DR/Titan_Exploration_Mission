class RobotMovement:
    def __init__(self, x, y, header):
        self.x = x
        self.y = y
        self.header = header


    def new_robot_position(self):
        if self.header == 'N':
            self.y = int(self.y) + 1
        elif self.header == 'S':
            self.y = int(self.y) - 1
        elif self.header == 'E':
            self.x = int(self.x) + 1
        elif self.header == 'W':
            self.x = int(self.x) - 1

        return self.x, self.y