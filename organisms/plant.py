from .base import Organism

class Plant(Organism):
    def __init__(self, identifier):
        super().__init__(identifier)
        self.name = "Plant"
        self.food_count = 1
        self.alive = True
        

    def plant_move(self, env):
        if self.name == "Plant":    
            if not self.alive:
                return
        
            row, col = self.position
            resources = env.check_resources(self.position)

            # If the plant has both water and sunlight, it reproduces
            if resources["water"] and resources["sunlight"]:
                self.food_count += 1
                if self.food_count >= 3:
                    self.food_count = 0
                    return True
                return False
            else:
                env.state_matrix[row, col] = env.EMPTY
