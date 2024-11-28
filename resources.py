import numpy as np

# The resource class allows for a resource to either have a structured distribution which will concentrate resources 
# into a specific subgrid within the grid, and random will randomly distribute resources
class Resource():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)

    # Will create a different distribution pattern based on the selected subgrid on every time ran
    def structured_resources(self, choices, weights, area):
        row_start, row_end, col_start, col_end = area
        # creates subgrid and distributes resources amongst it
        subgrid = np.random.choice(choices, size=(row_end - row_start, col_end - col_start), p=weights)
        # places subgrid onto main grid
        self.grid[row_start:row_end, col_start:col_end] = subgrid

    def random_resources(self, choices, weights):
        self.grid = np.random.choice(choices, size=(self.size, self.size), p=weights)
    
    def display(self):
        print(f"{self.name.capitalize()} Resource Grid:")
        print(self.grid)