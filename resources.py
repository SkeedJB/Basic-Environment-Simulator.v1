import numpy as np

# The resource class allows for a resource to either have a structured distribution which will concentrate resources 
# into a specific subgrid within the grid, and random will randomly distribute resources
class Resource():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)

    def structured_resources(self, choices, weights, area):
        row_start, row_end, col_start, col_end = area
        subgrid = np.random.choice(choices, size=(row_end - row_start, col_end - col_start), p=weights)
        self.grid[row_start:row_end, col_start:col_end] = subgrid

    def random_resources(self, choices, weights):
        choices = [0, 1, 2, 3, 4]
        weights = [0.20, 0.40, 0.60, 0.40, 0.20]
        return np.random.choice(choices, size=(self.size, self.size), p=weights)