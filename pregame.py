import pygame
import time
def make_instruction_screen(scr):
    # Background
    fline = pygame.image.load("kenney_racing-pack/PNG/Tiles/Asphalt road/road_asphalt70.png").convert()
    for x in range(0, scr.get_width(), fline.get_width()):
        for y in range(0, scr.get_height(), fline.get_height()):
            scr.blit(fline, (x, y))
    # Red Bike controls
    custom_font = pygame.font.SysFont('century', 25)
    text = custom_font.render('Player 1: You are the Red Motorcycle and you will drive with WASD', False,
                              (255, 69, 0))
    scr.blit(scr, (0, 0))
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2, scr.get_height() / 2 - text.get_height() / 2 - 100))
    # Welcome message
    custom_font = pygame.font.SysFont('century', 66)
    text = custom_font.render('Welcome to Stark Racing!', False, (0, 0, 0))
    scr.blit(scr, (0, 0))
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2, scr.get_height() / 2 - text.get_height() / 2 - 250))
    # Blue Bike controls
    custom_font = pygame.font.SysFont('century', 22)
    text = custom_font.render('Player 2: You are the Blue Motorcycle and you will steer with the Arrow Keys',
                              False, (0, 0, 255))
    scr.blit(scr, (0, 0))
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2, scr.get_height() / 2 - text.get_height() / 2 ))

    # Update the display (show to player).
    pygame.display.flip()
    time.sleep(3)

def make_count_down(background, scr):
# COUNTDOWN
    custom_font = pygame.font.SysFont('century', 128)
    text = custom_font.render('3', False, (255, 0, 0))
    scr.blit(background, (0, 0))
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2, scr.get_height() / 2 - text.get_height() / 2 - 100))
    time.sleep(1)
    # Update display
    pygame.display.flip()

    custom_font = pygame.font.SysFont('century', 136)
    text = custom_font.render('2', False, (255, 255, 255))
    scr.blit(background, (0, 0))
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2, scr.get_height() / 2 - text.get_height() / 2 - 100))
    time.sleep(1)
    # Update display
    pygame.display.flip()

    custom_font = pygame.font.SysFont('century', 136)
    text = custom_font.render('1', False, (0, 0, 255))
    scr.blit(background, (0, 0))
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2, scr.get_height() / 2 - text.get_height() / 2 - 100))
    time.sleep(1)
    # Update display
    pygame.display.flip()

    custom_font = pygame.font.SysFont('century', 136)
    text = custom_font.render('GO!!', False, (0, 0, 0))
    scr.blit(background, (0, 0))
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2, scr.get_height() / 2 - text.get_height() / 2 - 100))
    time.sleep(1)
    # Update display
    pygame.display.flip()
    # Allows for "GO!!" to display
    custom_font = pygame.font.SysFont('century', 128)
    text = custom_font.render('0', False, (0, 0, 0))
    scr.blit(background, (0, 0))
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2, scr.get_height() / 2 - text.get_height() / 2 - 100))
    time.sleep(1)
    # Update display
    pygame.display.flip()