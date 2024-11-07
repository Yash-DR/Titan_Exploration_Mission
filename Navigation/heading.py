class Header:
    def __init__(self, heading):
        self.heading = heading

    def left_new_heading(self):
        if self.heading == 'N':
            self.heading = 'W'
        elif self.heading == 'W':
            self.heading = 'S'
        elif self.heading == 'S':
            self.heading = 'E'
        else:
            self.heading = 'N'

        return self.heading

    def right_new_heading(self):
        if self.heading == 'N':
            self.heading = 'E'
        elif self.heading == 'E':
            self.heading = 'S'
        elif self.heading == 'S':
            self.heading = 'W'
        else:
            self.heading = 'N'

        return self.heading
