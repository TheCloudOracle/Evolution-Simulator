import random
import pygame


class Organism:
    """
    Define the organism.
    Each organism contains the following characteristics:
        1. It's location on a 2D plane
        2. It's genome which contains 8-character hexidemicals which govern the organism's behaviour
        3. A neural network brain which updates the genome
    """
    def __init__(self, window, world_size, genome_lenth=4):
        self.window = window
        self.world_size = world_size
        self.radius = 2
        self.location = self.x, self.y = random.randint(0, self.world_size[0]), random.randint(0, self.world_size[1])
        self.genome = [''.join(random.choices('0123456789ABCDEF', k=9)) for _ in range(genome_lenth)]
        self.brain = None # TODO: make this the neural network(s)
        # TODO: see if these should be random, or a fixed size
        self.speed_x = random.randint(-2, 2)
        self.speed_y = random.randint(-2, 2)
        # TODO: diversify the organisms by color
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

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

        return self.x, self.y

    def draw(self, window):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.radius)        