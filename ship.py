import pygame

class Ship:
    
    def __init__(self, ai_game):
        # initialize the ship & starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('images/player1.png')
        self.rect = self.image.get_rect()

        # start each new ship at bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)

    def update(self):
        # update the ships position
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed