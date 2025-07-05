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
    organisms = [Organism(window, world_size, configs, genome_length) for _ in range(population_size)]
    return organisms


def survival_area():
    sa = configs['survival_area_size']
    world_w, world_h = world_size

    rect_width = int(world_w * sa['width_ratio'])
    rect_height = int(world_h * sa['height_ratio'])
    rect_x = int(world_w * sa['x_offset_ratio'])
    rect_y = int(world_h * sa['y_offset_ratio'])

    return pygame.Rect(rect_x, rect_y, rect_width, rect_height)



def start():
    pygame.init()
    window = pygame.display.set_mode(world_size)
    orgs = init_orgs(window)
    clock = pygame.time.Clock()
    running = True

    while running:
        print(window.get_height())
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for org in orgs:
            org.move()


        window.fill((255, 255, 255))
        survival_rect = survival_area()
        pygame.draw.rect(window, (0, 255, 0), survival_rect)
        for org in orgs:
            org.draw(window)

        pygame.display.update()
    pygame.quit()



# load configs globally
configs = load_configs()
world_size = height, width = configs['world_size']['height'], configs['world_size']['width']
