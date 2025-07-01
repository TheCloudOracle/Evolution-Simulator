import json

from pathlib import Path
from  src.organism import *


def load_configs(filepath: Path='config.json'):
    filepath = Path(filepath)
    if not filepath.is_file():
        raise FileNotFoundError(f'Config file "config.json" is missing.')
    with open(filepath, 'r') as conf:
        configs = json.load(conf)
    
    return configs


def init_orgs(window):
    genome_length = configs['genome_length']
    population_size = configs['population']
    organisms = [Organism(window, world_size, genome_length) for _ in range(population_size)]
    return organisms


def start():
    pygame.init()
    window = pygame.display.set_mode(world_size)
    orgs = init_orgs(window)
    clock = pygame.time.Clock()
    running = True

    while running:
        positions = []
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for org in orgs:
            x, y = org.move()
            positions.append((x, y))
        
        for org in orgs:
            if (org.x, org.y) in positions:
                if org.x <= 0:
                    org.x += 10
                elif org.x >= world_size[0]:
                    org.x -= 10
                
                if org.y <= 0:
                    org.y += 1
                elif org.y >= world_size[1]:
                    org.y -= 1

        window.fill((255, 255, 255))
        for org in orgs:
            org.draw(window)

        pygame.display.update()
    pygame.quit()



# load configs globally
configs = load_configs()
world_size = height, width = configs['world_size']['height'], configs['world_size']['width']
