import numpy as np
from resources import Resource
from organisms import Prey, Predator, Plant

# Takes an int as a size and creates a grid based on that size
class Environment():

    EMPTY = 0
    PLANT = 1
    PREY = 2
    PREDATOR = 3

    TYPES = ["Prey", "Predator", "Plant"]

    def __init__(self, size):
        self.size = size
        self.state_matrix = np.zeros((size, size), dtype=int)
        self.resources = {}
        self.organisms = {}

    def check_resources(self, position):
        row, col = position
        water = self.resources["Water"].grid[row, col]
        sunlight = self.resources["Sunlight"].grid[row, col]
        return {"water": water, "sunlight": sunlight}
    
    def add_resource(self, resource_name):
        self.resources[resource_name] = Resource(resource_name, self.size)

    def add_organism(self, type):
        for type in self.TYPES:
            identifier = f"{type}_{len(self.organisms) + 1}"
            if type == "Prey":
                organism = Prey(identifier)
            elif type == "Predator":
                organism = Predator(identifier)
            elif type == "Plant":
                organism = Plant(identifier)
            self.organisms[identifier] = organism
            position = organism.get_start_position(self)
            
            if type == "Prey":
                self.state_matrix[position[0], position[1]] = self.PREY
            elif type == "Predator":
                self.state_matrix[position[0], position[1]] = self.PREDATOR
            elif type == "Plant":
                self.state_matrix[position[0], position[1]] = self.PLANT

    def display_resources(self):
        for resource in self.resources.values():
            resource.display()


    def update_state_matrix(self):
        # Reset the state matrix
        self.state_matrix = np.zeros((self.size, self.size), dtype=int)

        # Update positions of all organisms
        for _, organism in self.organisms.items():
            if organism.is_alive():
                pos = organism.get_current_position(self)
                if organism.name == "Prey":
                    self.state_matrix[pos[0], pos[1]] = self.PREY
                elif organism.name == "Predator":
                    self.state_matrix[pos[0], pos[1]] = self.PREDATOR
                elif organism.name == "Plant":
                    self.state_matrix[pos[0], pos[1]] = self.PLANT

        # Debug print
        for r in self.state_matrix:
            print(r)

    def display_state_matrix(self):
        state_matrix = {
            self.EMPTY: ".",
            self.PLANT: "🌱",
            self.PREY: "🐰",
            self.PREDATOR: "🦊"
        }

        print("\nEnvironment State:")
        for row in self.state_matrix:
            print(" ".join(state_matrix[cell] for cell in row))
