import pygame
import time


class Bike:

    def __init__(self, screen, color):

        # Draw bike with correct orientation and make color changeable.
        bike_name = f"kenney_racing-pack/PNG/Motorcycles/motorcycle_{color}.png"

        self.bike_img = pygame.image.load(bike_name).convert()
        self.bike_img.set_colorkey((0, 0, 0))
        self.bike_img = self.bike_img
        self.bike_img_left = pygame.transform.rotate(self.bike_img, 90)
        self.bike_img_down = pygame.transform.rotate(self.bike_img, 0)
        self.bike_img_right = pygame.transform.rotate(self.bike_img, 270)
        self.bike_img_up = pygame.transform.rotate(self.bike_img, 180)
        self.bike_x = 30
        self.bike_x_dir = 1
        self.bike_x_spd = screen.get_width()/(4*60)
        self.y_bnd = screen.get_height()
        self.bike_y = 5
        self.bike_y_dir = 1
        self.bike_y_spd = self.y_bnd/(3*60)


class BlueDrive(Bike):

    def __init__(self, screen, color):

        # Initialize parent class.
        super().__init__(screen, color)
        self.bike_x = 80
        # Keys
        self.key_up = 'not pressed'
        self.key_down = 'not pressed'
        self.key_left = 'not pressed'
        self.key_right = 'not pressed'

    def update_position(self, screen, events, background):

        # Update position based on keystrokes.
        for event in events:
            # See if user presses a key.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.key_up = 'pressed'

                if event.key == pygame.K_DOWN:
                    self.key_down = 'pressed'

                if event.key == pygame.K_LEFT:
                    self.key_left = 'pressed'

                if event.key == pygame.K_RIGHT:
                    self.key_right = 'pressed'

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.key_up = 'not pressed'

                if event.key == pygame.K_DOWN:
                    self.key_down = 'not pressed'

                if event.key == pygame.K_LEFT:
                    self.key_left = 'not pressed'

                if event.key == pygame.K_RIGHT:
                    self.key_right = 'not pressed'

        # Update blue bike based on status of my keys.
        if self.key_up == 'pressed':
            self.bike_y -= self.bike_y_spd
            self.bike_img = self.bike_img_down

        if self.key_down == 'pressed':
            self.bike_y += self.bike_y_spd
            self.bike_img = self.bike_img_up

        # Make left facing bike.
        if self.key_left == 'pressed':
            self.bike_x -= self.bike_x_spd
            self.bike_img = self.bike_img_left
        # Make right facing bike
        if self.key_right == 'pressed':
            self.bike_img = self.bike_img
            self.bike_x += self.bike_x_spd
            self.bike_img = self.bike_img_right

        # Check the position of the self.bike.
        if self.bike_x >= screen.get_width() - self.bike_img.get_width():
            self.bike_x = screen.get_width() - self.bike_img.get_width()

        if self.bike_x < 0:
            self.bike_x = 0

        if self.bike_y >= self.y_bnd:
            self.bike_y = self.y_bnd

        if self.bike_y < 0:
            self.bike_y = 0

        if self.bike_y >= screen.get_height() - self.bike_img.get_height():
            self.bike_y = screen.get_height() - self.bike_img.get_height()

            # CREATE TRACK BOUNDARIES

            # Right hand side first straight boundary
        barrier1 = pygame.Rect(128, 0, 60, 248)

        if self.bike_x >= barrier1.left - self.bike_img.get_width() and self.bike_x <= barrier1.right:
            if self.bike_y <= barrier1.height:
                self.bike_x = barrier1.left - self.bike_img.get_width()

        # Big middle boundary
        barrier5 = pygame.Rect(226, 0, 160, 496)
        if (self.bike_x >= barrier5.left - self.bike_img.get_width() and self.bike_x <= barrier5.right -
                self.bike_img.get_width()):
            if self.bike_y <= barrier5.height:
                self.bike_x = barrier5.left - self.bike_img.get_width()

        if self.bike_x <= barrier5.right and self.bike_x >= barrier5.left:
            if self.bike_y <= barrier5.height:
                self.bike_x = barrier5.right

        # Boundary separating final two turns
        barrier6 = pygame.Rect(530, 128, 110, 128)
        if (self.bike_x >= barrier6.left - self.bike_img.get_width() and self.bike_x <= barrier6.right -
                self.bike_img.get_width()):
            if self.bike_y >= barrier6.height:
                self.bike_x = barrier6.left - self.bike_img.get_width()

        if self.bike_x <= barrier6.right and self.bike_x >= barrier6.left:
            if self.bike_y >= barrier6.height:
                self.bike_x = barrier6.right

        # Far right boundary
        barrier9 = pygame.Rect(770, 0, 200, 650)
        if self.bike_x >= barrier9.left and self.bike_x <= barrier9.right:
            if self.bike_y <= barrier9.height:
                self.bike_x = barrier9.left

        # RACE sign on first straight
        barrier2 = pygame.Rect(0, 358, 88, 20)
        if self.bike_y >= barrier2.top - self.bike_img.get_width() and self.bike_y <= barrier2.bottom:
            if self.bike_x <= barrier2.right:
                self.bike_y = barrier2.top - self.bike_img.get_width()

        # End of chicane
        barrier7 = pygame.Rect(130, 476, 200, 20)
        if (self.bike_y >= barrier7.top - self.bike_img.get_width() and self.bike_y <= barrier7.bottom
                and self.bike_x <= barrier7.right and self.bike_x >= barrier7.left):
            self.bike_y = barrier7.top - self.bike_img.get_width()
        # Draw the self.bike.
        screen.blit(self.bike_img, (self.bike_x, self.bike_y))

        # Make it so that when Blue Bike crosses the finish line, game ends and "BLUE WINS!" appears
        finline = pygame.Rect(635, 600, 100, 200)
        if (self.bike_y >= finline.top - self.bike_img.get_width() and self.bike_x <= finline.right and self.bike_x >=
            finline.left):
            custom_font = pygame.font.SysFont('century', 128)
            text = custom_font.render('BLUE WINS!', False, (0, 0, 255))
            BlueDrive.bike_y = 1000
            BlueDrive.bike_x = 1000
            RedDrive.bike_y_spd = 0
            RedDrive.bike_x_spd = 0
            screen.blit(background, (0, 0))
            screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - text.get_height() / 2 - 100))
            pygame.display.flip()
            time.sleep(5)

class RedDrive(Bike):

    def __init__(self, screen, color):

        # Initialize parent class.
        super().__init__(screen, color)

        # Keys
        self.key_up = 'not pressed'
        self.key_down = 'not pressed'
        self.key_left = 'not pressed'
        self.key_right = 'not pressed'

    def update_position(self, screen, events, background):

        # Update position based on keystrokes.
        for event in events:
            # See if user presses a key.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.key_up = 'pressed'

                if event.key == pygame.K_s:
                    self.key_down = 'pressed'

                if event.key == pygame.K_a:
                    self.key_left = 'pressed'

                if event.key == pygame.K_d:
                    self.key_right = 'pressed'

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.key_up = 'not pressed'

                if event.key == pygame.K_s:
                    self.key_down = 'not pressed'

                if event.key == pygame.K_a:
                    self.key_left = 'not pressed'

                if event.key == pygame.K_d:
                    self.key_right = 'not pressed'

        # Update red bike based on status of my keys
        if self.key_up == 'pressed':
            self.bike_y -= self.bike_y_spd
            self.bike_img = self.bike_img_down

        if self.key_down == 'pressed':
            self.bike_y += self.bike_y_spd
            self.bike_img = self.bike_img_up
        # Make left facing bike
        if self.key_left == 'pressed':
            self.bike_x -= self.bike_x_spd
            self.bike_img = self.bike_img_left

        # Make right facing bike
        if self.key_right == 'pressed':
            self.bike_img = self.bike_img_right
            self.bike_x += self.bike_x_spd
            self.bike_img = self.bike_img_right
        # Check the position of the self.bike.
        if self.bike_x >= screen.get_width() - self.bike_img.get_width():
            self.bike_x = screen.get_width() - self.bike_img.get_width()

        if self.bike_x < 0:
            self.bike_x = 0

        if self.bike_y >= self.y_bnd:
            self.bike_y = self.y_bnd

        if self.bike_y < 0:
            self.bike_y = 0

        if self.bike_y >= screen.get_height() - self.bike_img.get_height():
            self.bike_y = screen.get_height() - self.bike_img.get_height()

        # CREATE TRACK BOUNDARIES

        #Right hand side first straight boundary
        barrier1 = pygame.Rect(128, 0, 60, 248)

        if self.bike_x >= barrier1.left - self.bike_img.get_width() and self.bike_x <= barrier1.right:
            if self.bike_y <= barrier1.height:
                self.bike_x = barrier1.left - self.bike_img.get_width()


        # Big middle boundary
        barrier5 = pygame.Rect(226, 0, 160, 496)
        if (self.bike_x >= barrier5.left - self.bike_img.get_width() and self.bike_x <= barrier5.right -
                self.bike_img.get_width()):
            if self.bike_y <= barrier5.height:
                self.bike_x = barrier5.left - self.bike_img.get_width()

        if self.bike_x <= barrier5.right and self.bike_x >= barrier5.left:
            if self.bike_y <= barrier5.height:
                self.bike_x = barrier5.right

        # Boundary separating final two turns
        barrier6 = pygame.Rect(530, 128, 110, 128 )
        if (self.bike_x >= barrier6.left - self.bike_img.get_width() and self.bike_x <= barrier6.right -
                self.bike_img.get_width()):
            if self.bike_y >= barrier6.height:
                self.bike_x = barrier6.left - self.bike_img.get_width()

        if self.bike_x <= barrier6.right and self.bike_x >= barrier6.left:
            if self.bike_y >= barrier6.height:
                self.bike_x = barrier6.right


        # Far right boundary
        barrier9 = pygame.Rect(770, 0, 200, 650)
        if self.bike_x >= barrier9.left and self.bike_x <= barrier9.right:
            if self.bike_y <= barrier9.height:
                self.bike_x = barrier9.left

        # RACE sign on first straight
        barrier2 = pygame.Rect(0, 358, 88, 20)
        if self.bike_y >= barrier2.top - self.bike_img.get_width() and self.bike_y <= barrier2.bottom:
            if self.bike_x <= barrier2.right:
                self.bike_y = barrier2.top - self.bike_img.get_width()

        # End of chicane

        barrier7 = pygame.Rect(130, 476, 200, 20)
        if (self.bike_y >= barrier7.top - self.bike_img.get_width() and self.bike_y <= barrier7.bottom
                and self.bike_x <= barrier7.right and self.bike_x >= barrier7.left):
            self.bike_y = barrier7.top - self.bike_img.get_width()
        # Draw the self.bike.
        screen.blit(self.bike_img, (self.bike_x, self.bike_y))

        # Make it so that when Red Bike crosses the finish line, game ends and "RED WINS!" appears
        finline = pygame.Rect(635, 600, 100, 200)
        if (self.bike_y >= finline.top - self.bike_img.get_width() and self.bike_x <= finline.right and self.bike_x >=
            finline.left):
            custom_font = pygame.font.SysFont('century', 128)
            text = custom_font.render('RED WINS!', False, (255, 0, 0))
            BlueDrive.bike_y = 1000
            BlueDrive.bike_x = 1000
            RedDrive.bike_y_spd = 0
            RedDrive.bike_x_spd = 0
            screen.blit(background, (0, 0))
            screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - text.get_height() / 2 - 100))
            pygame.display.flip()
            time.sleep(5)









