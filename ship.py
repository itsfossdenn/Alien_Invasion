import pygame

class Ship:
    
    def __init__(self, ai_game):
        # initialize the ship & starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('images/player1.png')
        self.rect = self.image.get_rect()

        # start each new ship at bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)

    def update(self):
        # update the ships position
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1