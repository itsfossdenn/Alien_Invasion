import sys, pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        #initialize game & Resources
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("datadenn's Alien Invasion!")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        #main loop to run the game
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

            self.screen.fill(self.bg_color)
            self.ship.blitme()

            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # detect keypresses & act accordingly
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # movement when key pressed
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        # movement after key release
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

    def _fire_bullet(self):
        # create a new bullet and add it to the Bullets group
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
            
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == "__main__":
    #create instance
    ai = AlienInvasion()
    ai.run_game()