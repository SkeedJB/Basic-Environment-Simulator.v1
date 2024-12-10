from environment import Environment
from resources import Resource
from organisms import Prey, Predator, Plant
import numpy as np
import time

# Creates environment
env = Environment(10)

# Adds resources to env
env.add_resource("Water")
env.add_resource("Sunlight")

# Sunlight resource parameters
sunlight_choices = [0, 1]
sunlight_weights = [0.5, 0.5]
sunlight_area = (1, 5, 1, 7)
env.resources["Sunlight"].structured_resources(sunlight_choices, sunlight_weights, sunlight_area)

# Water resource parameters
water_choices = [0, 1]
water_weights = [0.5, 0.5]
env.resources["Water"].random_resources(water_choices, water_weights)

# Adds organisms to env
for i in range(6):
    env.add_organism("organisms.prey.Prey")

for i in range(2):
    env.add_organism("organisms.predator.Predator") 

for i in range(6):
    env.add_organism("organisms.plant.Plant")


# Main Simulation Loop
for cycle in range(5):
    print(f"\nCycle {cycle + 1}")
    # Update organisms
    for identifier, organism in env.organisms.items():
        if organism.is_alive():
            if isinstance(organism, Prey):
                organism.prey_move(env)
            elif isinstance(organism, Predator):
                organism.predator_move(env)
            elif isinstance(organism, Plant):
                organism.plant_move(env)
                
    env.update_state_matrix()
    env.display_state_matrix()

    time.sleep(2)
