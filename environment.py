import numpy as np

# Takes an int as a size and creates a grid based on that size
class Environment():
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)