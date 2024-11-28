# Basic-Environment-Simulator.v1
 Simulates basic predator-prey interaction in a simple environment.

The simulation will simulate predator-prey relations in small, isolated ecosystems. Predators can eat prey and reproduce, prey can eat plants and reproduce, and plants need enough resources to be able to grow larger. 

# How the Simulation Works
The simulation begins with the formulation of a matrix filled with zeroes. This matrix is the environment, which will be made up of resources, plants, and animals. Each of these elements that make up the environment will be represented using different numbers to represent different states within that matrix, ie: [1, 0, 2] = [plant, empty, prey]

Predator will be able to eat prey, if prey is within 1 block distance in any direction. Prey will be able to eat plants, if plants within 1 block distance. If plant block has access to water and sun in any direction, plant may grow once mature. If either prey or predator can consume 3 of their respective food, they will reproduce. If they don't reproduce after 2 cycles, the animal will die.

# Real World Examples
## Siberian Lemmings and Arctic Foxes
Studies were done on the population and diet of a certain few animals who inhabit an isolated community in the Arctic Tundra. Within the study, researchers found that in one of these communities which involves the Arctic Fox and a few species of lemmings, the diet of the arctic foxes were primarily made up of two different species of lemming. Because of this dependency, the fox population would increase or decrease with a time lag of one year, based on the lemming population.
