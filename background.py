import pygame

def make_background(surface):

    # Load images

    straight = pygame.image.load("kenney_racing-pack/PNG/Tiles/Asphalt road/road_asphalt01.png").convert()
    grass = pygame.image.load("kenney_racing-pack/PNG/Tiles/Grass/land_grass11.png").convert()
    finish_line = pygame.image.load("kenney_racing-pack/PNG/Tiles/Asphalt road/road_asphalt42.png").convert()
    chicane1 = pygame.image.load("kenney_racing-pack/PNG/Tiles/Asphalt road/road_asphalt24.png").convert()
    chicane2 = pygame.image.load("kenney_racing-pack/PNG/Tiles/Asphalt road/road_asphalt05.png").convert()
    chicane3 = pygame.image.load("kenney_racing-pack/PNG/Tiles/Asphalt road/road_asphalt25.png").convert()
    chicane4 = pygame.image.load("kenney_racing-pack/PNG/Tiles/Asphalt road/road_asphalt03.png").convert()
    chicane5 = pygame.image.load("kenney_racing-pack/PNG/Tiles/Asphalt road/road_asphalt39.png").convert()
    rstraight = pygame.image.load("kenney_racing-pack/PNG/Tiles/Asphalt road/road_asphalt02.png").convert()
    lup = pygame.image.load("kenney_racing-pack/PNG/Tiles/Asphalt road/road_asphalt41.png").convert()
    stands = pygame.image.load("kenney_racing-pack/PNG/Objects/tribune_full.png").convert()
    tree = pygame.image.load("kenney_racing-pack/PNG/Objects/tree_small.png").convert()
    rtent = pygame.image.load("kenney_racing-pack/PNG/Objects/tent_red_large.png").convert()
    btent = pygame.image.load("kenney_racing-pack/PNG/Objects/tent_blue_large.png").convert()
    barrier = pygame.image.load("kenney_racing-pack/PNG/Objects/barrier_white_race.png").convert()

    # Make Black Pixels Transparent
    chicane1.set_colorkey((0, 0, 0))
    chicane2.set_colorkey((0, 0, 0))
    chicane3.set_colorkey((0, 0, 0))
    chicane4.set_colorkey((0, 0, 0))
    chicane5.set_colorkey((0, 0, 0))
    lup.set_colorkey((0, 0, 0))
    tree.set_colorkey((0, 0, 0))
    barrier.set_colorkey((0, 0, 0))
    # Grass Background
    for x in range(0, surface.get_width(), grass.get_width()):
        for y in range(0, surface.get_height(), grass.get_height()):
            surface.blit(grass, (x, y))
        # Track Pieces

    for x in range(0, surface.get_width(), chicane1.get_width()):
        surface.blit(chicane1, (0, 245))
    for x in range(0, surface.get_width(), straight.get_width()):
        surface.blit(straight, (0, 128))
    for x in range(0, surface.get_width(), straight.get_width()):
        surface.blit(straight, (0, 64))
    for x in range(0, surface.get_width(), finish_line.get_width()):
        surface.blit(finish_line, (0, 0))
    for x in range(0, surface.get_width(), chicane2.get_width()):
        surface.blit(chicane2, (110, 245))
    for x in range(0, surface.get_width(), chicane3.get_width()):
        surface.blit(chicane3, (110, 373))
    for x in range(0, surface.get_width(), chicane4.get_width()):
        surface.blit(chicane4, (0, 373))
    for x in range(0, surface.get_width(), chicane5.get_width()):
        surface.blit(chicane5, (0, 500))
    for x in range(0, surface.get_width(), rstraight.get_width()):
        surface.blit(rstraight, (128, 500))
    for x in range(0, surface.get_width(), rstraight.get_width()):
        surface.blit(rstraight, (256, 500))
    for x in range(0, surface.get_width(), lup.get_width()):
        surface.blit(lup, (384, 500))
    for x in range(0, surface.get_width(), straight.get_width()):
        surface.blit(straight, (384, 372))
    for x in range(0, surface.get_width(), straight.get_width()):
        surface.blit(straight, (384, 244))
    for x in range(0, surface.get_width(), straight.get_width()):
        surface.blit(straight, (384, 116))
    for x in range(0, surface.get_width(), chicane4.get_width()):
        surface.blit(chicane4, (384, -8))
    for x in range(0, surface.get_width(), rstraight.get_width()):
        surface.blit(rstraight, (512, -8))
    for x in range(0, surface.get_width(), chicane2.get_width()):
        surface.blit(chicane2, (640, -8))
    for x in range(0, surface.get_width(), straight.get_width()):
        surface.blit(straight, (640, 120))
    for x in range(0, surface.get_width(), straight.get_width()):
        surface.blit(straight, (640, 248))
    for x in range(0, surface.get_width(), straight.get_width()):
        surface.blit(straight, (640, 376))
    for x in range(0, surface.get_width(), finish_line.get_width()):
        surface.blit(finish_line, (640, 504))
    for x in range(0, surface.get_width(), straight.get_width()):
        surface.blit(straight, (640, 632))
    # Decorations
    for x in range(0, surface.get_width(), barrier.get_width()):
        surface.blit(barrier, (525, 550))
    for x in range(0, surface.get_width(), barrier.get_width()):
        surface.blit(barrier, (150, 40))
    for x in range(0, surface.get_width(), stands.get_width()):
        surface.blit(stands, (235, 440))
    for x in range(0, surface.get_width(), tree.get_width()):
        surface.blit(tree, (150, 100))
    for x in range(0, surface.get_width(), rtent.get_width()):
        surface.blit(rtent, (545, 400))
    for x in range(0, surface.get_width(), btent.get_width()):
        surface.blit(btent, (545, 464))
    for x in range(0, surface.get_width(), rtent.get_width()):
        surface.blit(rtent, (545, 272))
    for x in range(0, surface.get_width(), btent.get_width()):
        surface.blit(btent, (545, 336))
    for x in range(0, surface.get_width(), barrier.get_width()):
        surface.blit(barrier, (-10, 350))
