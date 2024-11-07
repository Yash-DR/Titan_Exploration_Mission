class GridBoundary:
    def __init__(self, total_grid_size):
        self.total_grid_size = total_grid_size
        self.x_max = self.total_grid_size[0]
        self.y_max = self.total_grid_size[1]
        self.x_min = 0
        self.y_min = 0


    def coordinate_position(self, initial_coordinate):
        if self.x_min <= int(initial_coordinate[0]) <= self.x_max and self.y_min <= int(initial_coordinate[1]) <= self.y_max:
            return True
        else:
            return False



