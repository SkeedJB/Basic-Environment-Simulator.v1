from environment import Environment
from resources import Resource
import numpy as np
# Creates environment
env = Environment(7)

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
water_weights = [0.6, 0.4]
env.resources["Water"].random_resources(water_choices, water_weights)

# Displays all resources in environment
env.display_resources()