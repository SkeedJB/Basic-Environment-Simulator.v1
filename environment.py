import numpy as np
from resources import Resource

# Takes an int as a size and creates a grid based on that size
class Environment():
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)
        self.resources = {}

    def add_resource(self, resource_name):
        self.resources[resource_name] = Resource(resource_name, self.size)

    def display_resources(self):
        for resource in self.resources.values():
            resource.display()
