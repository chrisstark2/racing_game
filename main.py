import pygame
from pygame import mixer
import sys
import time
from racing_utils import BlueDrive, RedDrive
from pregame import make_count_down, make_instruction_screen
from background import make_background

# Initialize Pygame
pygame.init()
mixer.init()

# Create Pygame clock.
clock = pygame.time.Clock()

# Clear terminal output.
for ii in range(0, 10):
    print()

print('\nRunning main.py.')
print('-------------------------------------------')

# Specify screen dimensions.
scr_wid = 800  # (px)
scr_hgt = 650  # (px)


mixer.music.load("kenney_racing-pack/on-the-road-to-the-eighties-131722.ogg")
mixer.music.play()
# Create the screen.
scr = pygame.display.set_mode((scr_wid, scr_hgt))
pygame.display.set_caption('Stark Racing')
background = scr.copy()
make_background(background)
make_instruction_screen(scr)
make_count_down(background, scr)

# Create blue bike
blue = BlueDrive(scr, 'blue')
# Create red bike
red = RedDrive(scr, 'red')

running = True
while running:

    events = pygame.event.get()
    t1 = time.time()
    # Get events happening in window.
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Put background on scr
    scr.blit(background, (0, 0))
    # Put blue bike on scr
    blue.update_position(scr, events, background)
    # Put red bike on scr
    red.update_position(scr, events, background)
    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

