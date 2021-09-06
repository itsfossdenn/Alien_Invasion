import sys, pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        #initialize game & Resources
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("datadenn's Alien Invasion!")

        self.ship = Ship(self)

        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        #main loop to run the game
        while True:
            self._check_events()
            self.ship.update()
            self._check_screen()

            self.screen.fill(self.bg_color)
            self.ship.blitme()

            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # detect keypresses & act accordingly
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def _check_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    #create instance
    ai = AlienInvasion()
    ai.run_game()