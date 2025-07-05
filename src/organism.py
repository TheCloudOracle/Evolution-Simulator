import random
import pygame
import math
import src.neural_network


class Organism:
    """
    Define the organism.
    Each organism contains the following characteristics:
        1. It's location on a 2D plane
        2. It's genome which contains 8-character hexidemicals which govern the organism's behaviour
        3. A neural network brain which updates the genome
    """
    def __init__(self, window, world_size, config, genome_lenth=4):
        self.window = window
        self.world_size = world_size
        self.radius = 2
        self.location = self.x, self.y = random.randint(0, self.world_size[0]), random.randint(0, self.world_size[1])
        self.genome = [''.join(random.choices('0123456789ABCDEF', k=9)) for _ in range(genome_lenth)]
        # TODO: see if these should be random, or a fixed size
        self.speed_x = random.randint(-2, 2)
        self.speed_y = random.randint(-2, 2)
        # TODO: diversify the organisms by color
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # calculations
        self.border_distance_x = min(self.x, world_size[0] - self.x)
        self.border_distance_y = min(self.y, world_size[1] - self.y)

        # Sensory neurons
        self.sensory_neurons = {
            'Rnd': random.random(), # Random input
            'pop': config['population'], # Population Density
            'BDy': self.border_distance_y, # Distance to north/south border
            'BDx': self.border_distance_x, # Distance to east/west border
            'BD': min(self.border_distance_x, self.border_distance_y), # Distance to nearest border
            'Lx': self.x, # East/west location
            'Ly': self.y # north/south location
        }

        # Action neurons
        self.action_neurons = {
            'LPD': random.random(), # long probe distance
            'kill': random.random(), # kill forward neighbor
            'osc': random.random(), # set oscilator period
            'SG': random.random(), # emit pheremones
            'Resx': random.random(), # responsiveness (speed) east/west
            'Resy': random.random(), # responsiveness (speed) north/south
            'Mfd': random.random(), # move forward
            'Mrn': random.random(), # Move random
            'Mrv': random.random(), # Move reverse
            'Mx': random.random(), # Move east/west (+/-)
            'My': random.random() # Move north/south (+/-)
        }

        self.num_input_neurons = len(self.sensory_neurons)
        self.num_output_neurons = len(self.action_neurons)
        self.brain = list(self.action_neurons.values()) # Update using the neural network

      
    def __repr__(self):
        return f"""
                Creature:\n
                location: {self.location}
                genome: {self.genome}
                brain: {self.brain}
                speed x: {self.speed_x}
                speed y: {self.speed_y}
                self.color: {self.color}
                """
    
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= 0 or self.x >= self.world_size[0]:
            self.speed_x = 0
            self.speed_y = 0
        if self.y <= 0 or self.y >= self.world_size[1]:
            self.speed_y = 0
            self.speed_x = 0

    def draw(self, window):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.radius)        

    def gene_decoding(self, gene):
        sensory_neurons_keys = self.sensory_neurons.keys()
        action_neurons_keys = self.action_neurons.keys()
        # Convert gene to decimal
        binary_repr = bin(int(gene, 16))[2:]
        # Determine the input neuron - first byte of gene
        sensory_neuron_index = int(binary_repr[:8], 2) % self.num_input_neurons
        sensory_neuron_key = list(sensory_neurons_keys)[sensory_neuron_index] # Use this to index the dictionary
        # Deterome the output neuron - second byte of gene
        action_neuron_index = int(binary_repr[8:16], 2) % self.num_output_neurons
        action_neuron_key = list(action_neurons_keys)[action_neuron_index]
        weight = 1 / (1 + math.log(1 + abs(int(binary_repr[16:], 2))))
 
        return sensory_neuron_key, action_neuron_key, weight