import random

class Organism():
    def __init__(self, identifier):
        self.identifier = identifier
        self.position = None
        self.alive = True

    def is_alive(self):
        return self.alive
    
    def get_start_position(self, env):
        self.position = (random.randint(0, env.size - 1), random.randint(0, env.size - 1))
        return self.position
    
    def get_current_position(self, env):
        return self.position
