import numpy as np
from .base import Organism

class Prey(Organism):
    def __init__(self, identifier):
        super().__init__(identifier)
        self.name = "Prey"
        self.food_count = 2
        self.cycles_without_food = 0
        self.health = 100
        self.hunger_damage = 10
        self.starvation_threshold = 0
        self.alive = True
        
    def is_alive(self):
        if self.alive:
            return True
        else:
            return False
            
    def update_health(self):
        if self.food_count == 0:
            self.health -= self.hunger_damage

    def get_start_position(self, env):
        self.position = (np.random.randint(0, env.size), np.random.randint(0, env.size))
        return self.position
    
    def get_current_position(self, env):  # Changed from just (self) to (self, env)
        return self.position

    def prey_move(self, env):
        if self.name == "Prey":
            if not self.alive:
                return
            
            current_row, current_col = self.position
            possible_moves = []

            # Checks all 8 possible moves from adjacent cells
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    new_row = current_row + dr
                    new_col = current_col + dc

                    # Checks if the new position is within the environment bounds
                    if 0 <= new_row < env.size and 0 <= new_col < env.size:
                        if env.state_matrix[new_row, new_col] == env.PLANT:
                            self.food_count += 1
                            possible_moves.append((new_row, new_col))

            if possible_moves:
                self.position = possible_moves[np.random.randint(0, len(possible_moves))]
                self.cycles_without_food = 0
            else:
                self.cycles_without_food += 1
                new_row = min(max(current_row + np.random.randint(-1, 2), 0), env.size - 1)
                new_col = min(max(current_col + np.random.randint(-1, 2), 0), env.size - 1)
                self.position = (new_row, new_col)

            # If the prey has eaten 3 times, it reproduces
            if self.food_count >= 3:
                self.food_count = 0
                return True
            # If the prey has not eaten for 2 cycles, it dies
            elif self.cycles_without_food >= 3:
                self.alive = False  
            return False